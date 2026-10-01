# Prototipo de Diagnóstico e Inspección HTTP

**Asignatura:** Programación sobre redes  
**Trabajo Práctico:** N°12
**Curso:** 6° Año 7ma | **Grupo:** N° 2  
**Integrantes:** Elias Ramos, Erik Atusparia, Mateo Florentin, Tiziano Ciocca  

## Breve Descripción del Producto

Este software es un prototipo de utilidad de diagnóstico de red compatible de forma nativa con **Windows** y **Linux**. Ha sido diseñado para auditar, probar e inspeccionar servicios web HTTP/HTTPS:

- Identificación y análisis de **Tipos MIME** (`Content-Type`).
- Inspección de cabeceras de **Cookies** (`Set-Cookie`) y directivas de seguridad (`Secure`, `HttpOnly`).
- Detección de mecanismos de **Redirección HTTP** (códigos `3xx` y cabeceras `Location`).
- Envío de peticiones HTTP arbitrarias (`GET`, `POST`, `PUT`, `DELETE`) con soporte para **Autenticación HTTP Básica** (Basic Auth).

Está implementado íntegramente en Python utilizando exclusivamente su Biblioteca Estándar (PSL), garantizando ejecución inmediata sin dependencias externas.

---

## Requisitos e Instrucciones de Instalación y Ejecución

### Entorno de Ejecución
- **Lenguaje:** Python 3.6 o superior.
- **Dependencias externas:** Ninguna (utiliza paquetes nativos como `urllib`, `http.cookiejar` y `argparse`).
- **Sistemas Operativos Compatibles:** Windows 10/11, distribuciones Linux (Ubuntu, Debian, Fedora, etc.) y macOS.

### Pasos para Ejecutar

1. **Clonar el repositorio o descargar el código:**
   ```bash
   git clone <https://github.com/tiziicioccaa/tp13-redes-bottle/tree/main>
   cd <TP-12-BOTTLE>
2. **Ejecutar el programa directamente desde la terminal / consola de comandos:**
 ** Uso directo sin parámetros:**
     python main.py
**Uso pasando una URL de inicio mediante parámetros de terminal:**
     python main.py -u http://localhost:8080

Lista de Operaciones Disponibles
​El prototipo cuenta con un menú interactivo basado en consola de comandos. A continuación se detallan las operaciones disponibles:

**1.​[Diagnóstico] Auditar Estado HTTP y Redirecciones (3xx / Location):**
    **​Descripción:** Realiza una petición hacia la URL destino, verifica el código de estado retornado e identifica si el servidor emitió un comando de redirección (como 301 o 302), informando la URL final alcanzada.  
**2.​[Diagnóstico]Inspeccionar Tipos MIME y cookies 
   ​**Descripción:** Analiza la cabecera Content-Type para clasificar el tipo MIME del recurso (text/html, application/json, etc.) y extrae las cookies enviadas por el servidor mediante Set-Cookie, evaluando el cumplimiento de parámetros de seguridad (Secure, HttpOnly).  
**3.​[Operación de Entrada/Obtención de Datos]** 
 **Enviar Petición HTTP Personalizada:**
      **​Descripción:** 
          Permite al usuario interactuar activamente con el servidor web enviando parámetros en el cuerpo de la petición (POST/PUT) y autenticarse dinámicamente mediante credenciales HTTP Basic Auth (urllib.request.HTTPBasicAuthHandler). Retorna el código de respuesta y una vista previa del cuerpo recibido.  
**4.​Cambiar URL de destino:**
  ​. Descripción: Permite redefinir la dirección  IP o dominio a evaluar sin reiniciar la aplicación.
**​5.Salir:**
  ​**Descripción:** 
         Finaliza la ejecución del  prototipo.
