**Asignatura:** Programación sobre redes  
**Trabajo Práctico:** N°13 - Preguntas Frecuentes (HTTP, Cookies, Redirecciones, Bottle)[span_0](start_span)[span_0](end_span)  
**Curso:** 6° Año 7ma | **Grupo:** N° 2[span_1](start_span)[span_1](end_span)  
**Integrantes:** Elias Ramos, Erik Atusparia, Mateo Florentin, Tiziano Ciocca[span_2](start_span)[span_2](end_span)  

---

## Breve Descripción del Producto

Este software es un prototipo de utilidad de diagnóstico de red compatible de forma nativa con **Windows** y **Linux**. Ha sido diseñado para auditar, probar e inspeccionar servicios web HTTP/HTTPS evaluando los conceptos trabajados en el TP N°13:

- Identificación y análisis de **Tipos MIME** (`Content-Type`)[span_3](start_span)[span_3](end_span).
- Inspección de cabeceras de **Cookies** (`Set-Cookie`) y directivas de seguridad (`Secure`, `HttpOnly`)[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).
- Detección de mecanismos de **Redirección HTTP** (códigos `3xx` y cabeceras `Location`)[span_6](start_span)[span_6](end_span).
- Envío de peticiones HTTP arbitrarias (`GET`, `POST`, `PUT`, `DELETE`) con soporte para **Autenticación HTTP Básica** (Basic Auth)[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span).

Está implementado íntegramente en Python utilizando exclusivamente su Biblioteca Estándar (PSL), garantizando ejecución inmediata sin dependencias externas[span_9](start_span)[span_9](end_span).

---

## Requisitos e Instrucciones de Instalación y Ejecución

### Entorno de Ejecución
- **Lenguaje:** Python 3.6 o superior.
- **Dependencias externas:** Ninguna (utiliza paquetes nativos como `urllib`, `http.cookiejar` y `argparse`)[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span).
- **Sistemas Operativos Compatibles:** Windows 10/11, distribuciones Linux (Ubuntu, Debian, Fedora, etc.) y macOS.

### Pasos para Ejecutar

1. **Clonar el repositorio o descargar el código:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>

 * Ejecutar el programa directamente desde la terminal / consola de comandos:
   * Uso directo sin parámetros:
     python main.py

   * Uso pasando una URL de inicio mediante parámetros de terminal:
     python main.py -u http://localhost:8080

     (En sistemas Linux puede ser necesario usar python3 main.py)
Lista de Operaciones Disponibles
El prototipo cuenta con un menú interactivo basado en consola de comandos. A continuación se detallan las operaciones disponibles:
 * [Diagnóstico] Auditar Estado HTTP y Redirecciones (3xx / Location):
   * Descripción: Realiza una petición hacia la URL destino, verifica el código de estado retornado e identifica si el servidor emitió un comando de redirección (como 301 o 302), informando la URL final alcanzada.
 * [Diagnóstico] Inspeccionar Tipos MIME y Cookies:
   * Descripción: Analiza la cabecera Content-Type para clasificar el tipo MIME del recurso (text/html, application/json, etc.) y extrae las cookies enviadas por el servidor mediante Set-Cookie, evaluando el cumplimiento de parámetros de seguridad (Secure, HttpOnly).
 * [Operación de Entrada/Obtención de Datos] Enviar Petición HTTP Personalizada:
   * Descripción: Permite al usuario interactuar activamente con el servidor web enviando parámetros en el cuerpo de la petición (POST/PUT) y autenticarse dinámicamente mediante credenciales HTTP Basic Auth (urllib.request.HTTPBasicAuthHandler). Retorna el código de respuesta y una vista previa del cuerpo recibido.
 * Cambiar URL de destino:
   * Descripción: Permite redefinir la dirección IP o dominio a evaluar sin reiniciar la aplicación.
 * Salir:
   * Descripción: Finaliza la ejecución del prototipo.

