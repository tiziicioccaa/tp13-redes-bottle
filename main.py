"""Herramienta interactiva de diagnóstico e inspección de servicios HTTP."""

import sys
import argparse
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
from typing import Dict, Any


def diagnostico_estado_y_redireccion(url: str) -> Dict[str, Any]:
    """Obtiene el estado HTTP y registra si la solicitud siguió una redirección."""
    resultado = {
        "url_original": url,
        "codigo_estado": None,
        "redireccionado": False,
        "url_final": url,
        "cabeceras": {}
    }
    
    # urllib sigue las redirecciones automáticamente; este manejador registra
    # cuándo ocurren y cuál es su destino, conservando ese comportamiento.
    class NoRedirectionHandler(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            resultado["redireccionado"] = True
            resultado["url_final"] = newurl
            return super().redirect_request(req, fp, code, msg, headers, newurl)

    opener = urllib.request.build_opener(NoRedirectionHandler())
    req = urllib.request.Request(url, headers={'User-Agent': 'HTTP-Diagnostic-Tool/1.0'})

    try:
        with opener.open(req, timeout=10) as response:
            # La URL de la respuesta permite informar el destino final tras redirecciones.
            resultado["codigo_estado"] = response.getcode()
            resultado["url_final"] = response.geturl()
            resultado["cabeceras"] = dict(response.info())
            if resultado["url_final"] != url:
                resultado["redireccionado"] = True
    except urllib.error.HTTPError as e:
        # HTTPError representa una respuesta HTTP recibida (por ejemplo, 404),
        # por lo que su código y sus cabeceras también son datos del diagnóstico.
        resultado["codigo_estado"] = e.code
        resultado["cabeceras"] = dict(e.headers)
    except urllib.error.URLError as e:
        # URLError indica que no se pudo completar la comunicación con el servidor.
        resultado["error"] = str(e.reason)

    return resultado


def diagnostico_cookies_y_mime(url: str) -> Dict[str, Any]:
    """Inspecciona el tipo MIME y las cookies que entrega el servidor."""
    resultado = {
        "tipo_mime": "Desconocido",
        "cookies_recibidas": [],
        "seguridad_cookies": []
    }

    # CookieJar procesa las cabeceras Set-Cookie y expone los atributos de cada cookie.
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(url, headers={'User-Agent': 'HTTP-Diagnostic-Tool/1.0'})

    try:
        with opener.open(req, timeout=10) as response:
            headers = response.info()
            # El tipo MIME se obtiene de Content-Type, sin incluir parámetros como charset.
            resultado["tipo_mime"] = headers.get_content_type()
            
            # Se conservan atributos útiles para revisar las directivas de seguridad.
            for cookie in cj:
                info_cookie = {
                    "nombre": cookie.name,
                    "valor": cookie.value,
                    "dominio": cookie.domain,
                    "path": cookie.path,
                    "secure": cookie.secure,
                    "httponly": cookie.has_nonstandard_attr('HttpOnly')
                }
                resultado["cookies_recibidas"].append(info_cookie)

    except Exception as e:
        resultado["error"] = str(e)

    return resultado


def operacion_peticion_personalizada(url: str, metodo: str = "GET", datos_form: dict = None, usuario: str = None, clave: str = None) -> Dict[str, Any]:
    """Envía una petición HTTP, opcionalmente con formulario o autenticación básica.

    Los datos de formulario se codifican como application/x-www-form-urlencoded.
    El cuerpo de respuesta se limita a 500 caracteres para mostrarlo en la consola.
    """
    resultado = {
        "metodo": metodo,
        "codigo_estado": None,
        "cuerpo_respuesta": None
    }

    # La autenticación se configura solo cuando se proporcionan ambos campos.
    if usuario and clave:
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, url, usuario, clave)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
    else:
        opener = urllib.request.build_opener()

    # Solo estos métodos reciben los datos de formulario preparados por el menú.
    data_bytes = None
    if datos_form and metodo.upper() in ["POST", "PUT", "PATCH"]:
        data_bytes = urllib.parse.urlencode(datos_form).encode('utf-8')

    req = urllib.request.Request(url, data=data_bytes, method=metodo.upper())
    req.add_header('User-Agent', 'HTTP-Diagnostic-Tool/1.0')

    try:
        with opener.open(req, timeout=10) as response:
            resultado["codigo_estado"] = response.getcode()
            cuerpo = response.read().decode('utf-8', errors='replace')
            # Evita volcar respuestas extensas completas en la terminal.
            resultado["cuerpo_respuesta"] = cuerpo[:500] + ("..." if len(cuerpo) > 500 else "")
    except urllib.error.HTTPError as e:
        # También se muestra el cuerpo devuelto por errores HTTP, como 401 o 404.
        resultado["codigo_estado"] = e.code
        resultado["cuerpo_respuesta"] = e.read().decode('utf-8', errors='replace')[:500]
    except urllib.error.URLError as e:
        resultado["error"] = str(e.reason)

    return resultado


def menu_interactivo(url_defecto: str = None):
    """Ejecuta el menú de consola y permite cambiar la URL entre operaciones."""
    print("==========================================================")
    print("    HERRAMIENTA DE DIAGNÓSTICO E INSPECCIÓN DE RED (HTTP)  ")
    print("==========================================================")

    url_actual = url_defecto if url_defecto else ""

    while True:
        if not url_actual:
            url_actual = input("\n[+] Ingrese la URL de destino (ej: http://localhost:8080 o https://httpbin.org): ").strip()
            # Para las URL ingresadas en el menú, se asume HTTP si falta el esquema.
            if not url_actual.startswith("http://") and not url_actual.startswith("https://"):
                url_actual = "http://" + url_actual

        print(f"\n--- URL Actual: {url_actual} ---")
        print("1. [Diagnóstico] Auditar Estado HTTP y Redirecciones (3xx / Location)")
        print("2. [Diagnóstico] Inspeccionar Tipos MIME (Content-Type) y Cookies (Set-Cookie)")
        print("3. [Operación] Enviar Petición HTTP Personalizada (GET/POST/PUT/DELETE / Auth)")
        print("4. Cambiar URL de destino")
        print("5. Salir")

        opcion = input("\nSeleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\nEjecutando diagnóstico de estado y redirección...")
            res = diagnostico_estado_y_redireccion(url_actual)
            print(f" -> Código de Estado: {res.get('codigo_estado')}")
            print(f" -> Posee Redirección: {'Sí' if res.get('redireccionado') else 'No'}")
            print(f" -> URL Final: {res.get('url_final')}")
            if "error" in res:
                print(f" -> Error: {res['error']}")

        elif opcion == "2":
            print("\nEjecutando diagnóstico de MIME y cookies...")
            res = diagnostico_cookies_y_mime(url_actual)
            print(f" -> Tipo MIME Detectado: {res.get('tipo_mime')}")
            cookies = res.get("cookies_recibidas", [])
            print(f" -> Cookies detectadas ({len(cookies)}):")
            for c in cookies:
                print(f"    - [{c['nombre']}={c['valor']}] | Dominio: {c['dominio']} | Secure: {c['secure']} | HttpOnly: {c['httponly']}")
            if "error" in res:
                print(f" -> Error: {res['error']}")

        elif opcion == "3":
            print("\n--- Operación de Datos HTTP ---")
            metodo = input("Ingrese el método HTTP (GET/POST/PUT/DELETE) [GET]: ").strip().upper() or "GET"
            
            # El menú permite cargar un único campo de formulario para estos métodos.
            datos = {}
            if metodo in ["POST", "PUT", "PATCH"]:
                clave_p = input("Ingrese clave de parámetro de formulario (opcional): ").strip()
                if clave_p:
                    valor_p = input(f"Ingrese valor para '{clave_p}': ").strip()
                    datos[clave_p] = valor_p

            usar_auth = input("¿Requiere Autenticación HTTP Básica? (s/N): ").strip().lower()
            usr, pwd = None, None
            if usar_auth == 's':
                usr = input("Usuario: ").strip()
                pwd = input("Contraseña: ").strip()

            # Se informa el código y una vista previa del cuerpo de respuesta.
            print("\nEnviando petición...")
            res = operacion_peticion_personalizada(url_actual, metodo=metodo, datos_form=datos, usuario=usr, clave=pwd)
            print(f" -> Código de Estado: {res.get('codigo_estado')}")
            print(" -> Respuesta recibida:")
            print(res.get("cuerpo_respuesta"))

        elif opcion == "4":
            # La siguiente vuelta del menú vuelve a solicitar la URL de destino.
            url_actual = ""

        elif opcion == "5":
            print("\nSaliendo de la aplicación...")
            sys.exit(0)
        else:
            print("\n[!] Opción no válida. Intente nuevamente.")


def main():
    """Configura los argumentos de línea de comandos e inicia el menú."""
    parser = argparse.ArgumentParser(
        description="Herramienta CLI de Diagnóstico e Inspección HTTP según contenidos del TP N°13."
    )
    parser.add_argument(
        "-u", "--url", 
        type=str, 
        help="URL inicial sobre la cual ejecutar las operaciones de diagnóstico."
    )
    
    args = parser.parse_args()
    menu_interactivo(url_defecto=args.url)


# Permite importar las funciones sin iniciar el menú interactivo.
if __name__ == "__main__":
    main()
