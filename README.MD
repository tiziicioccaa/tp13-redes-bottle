# Herramienta de diagnóstico e inspección HTTP

**Asignatura:** Programación sobre redes | **Trabajo Práctico:** N.º 13

**Curso:** 6.º Año, 7.ª | **Grupo:** N.º 2

**Integrantes:** Elias Ramos, Erik Atusparia, Mateo Florentin y Tiziano Ciocca

## Descripción

Aplicación de consola para inspeccionar servicios web HTTP y HTTPS. Permite consultar estados y redirecciones, revisar el tipo MIME y las cookies recibidas, y enviar peticiones HTTP con datos de formulario o autenticación HTTP Básica.

## Requisitos

- **Python:** 3.6 o posterior. El código utiliza f-strings, disponibles desde Python 3.6.
- **Dependencias:** solo la biblioteca estándar de Python; no es necesario instalar paquetes con `pip`.
- **Git:** necesario únicamente si se usa el comando `git clone` para descargar el proyecto.
- **Sistemas operativos:** Windows 10/11, Linux y macOS, con Python instalado y disponible desde una terminal.
- **Conexión de red:** necesaria para consultar servidores remotos. También se pueden probar servicios HTTP que se ejecuten en la misma PC.

## Instalación y ejecución

1. Instala Python 3.6 o posterior desde [python.org](https://www.python.org/downloads/) si todavía no está instalado. En Windows puedes comprobarlo con `py --version`; en Linux o macOS, con `python3 --version`.
2. Descarga el proyecto desde la terminal:

   ```bash
   git clone https://github.com/tiziicioccaa/tp13-redes-bottle.git
   cd tp13-redes-bottle
   ```

   Si ya tienes el repositorio descargado, abre una terminal en la carpeta que contiene `main.py`.
3. Ejecuta el menú:

   **Windows (PowerShell o Símbolo del sistema):**

   ```powershell
   py main.py
   ```

   **Linux o macOS:**

   ```bash
   python3 main.py
   ```

   En cualquiera de los sistemas también puedes indicar una URL inicial:

   ```bash
   py main.py -u https://github.com
   ```

   En Linux o macOS, sustituye `py` por `python3`. El argumento `-u` también puede escribirse `--url`; proporciona la URL completa, incluido `http://` o `https://`.

## Menú y operaciones

Al iniciar sin `-u`, el programa solicita una URL. Si se ingresa una dirección sin esquema, el menú le antepone `http://`. La URL actual se muestra sobre las opciones y se reutiliza hasta que se cambie.

1. **Auditar estado HTTP y redirecciones:** envía una petición a la URL actual y muestra el código HTTP, si se siguió una redirección y la URL final. Las redirecciones se siguen automáticamente.
2. **Inspeccionar MIME y cookies:** muestra el tipo MIME de la respuesta y las cookies recibidas. Para cada cookie informa nombre, valor, dominio y los atributos `Secure` y `HttpOnly`.
3. **Enviar petición HTTP personalizada:**
   - Ingresa un método. El menú ofrece `GET`, `POST`, `PUT` y `DELETE`; también se puede ingresar `PATCH` u otro método aceptado por `urllib`.
   - Para `POST`, `PUT` o `PATCH`, puedes ingresar un único nombre y valor de parámetro; dejar vacío el nombre no agrega datos. Los parámetros se envían codificados como formulario (`application/x-www-form-urlencoded`).
   - Indica si el recurso requiere autenticación HTTP Básica y, si corresponde, proporciona usuario y contraseña. La autenticación se configura solo si ambos campos tienen contenido.
   - El resultado muestra el código HTTP y hasta 500 caracteres del cuerpo de respuesta.
4. **Cambiar URL de destino:** solicita otra URL y vuelve al menú con ese nuevo destino. Si no se especifica el esquema, se antepone `http://`.
5. **Salir:** finaliza la aplicación.

## Límites e información importante

- Cada solicitud tiene un tiempo de espera máximo de 10 segundos.
- La operación de petición personalizada no permite definir cabeceras arbitrarias, enviar JSON ni agregar varios parámetros desde el menú. `GET` y `DELETE` no solicitan datos de formulario.
- La autenticación implementada es HTTP Básica. Usa `https://` para proteger las credenciales durante el transporte; HTTP sin cifrado no las protege.
- Al usar `-u`/`--url`, incluye el esquema en la URL; el prefijo automático solo se aplica a las direcciones escritas en el menú.
- Los errores HTTP devueltos por el servidor se muestran como respuestas con su código de estado. Los errores de conexión se informan en las operaciones de diagnóstico o petición.
