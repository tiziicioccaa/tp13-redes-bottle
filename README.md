# Prototipo de Diagnóstico e Inspección HTTP

**Asignatura:** Programación sobre redes  
**Trabajo Práctico:** N°13 - Preguntas Frecuentes (HTTP, Cookies, Redirecciones, Bottle)  
**Curso:** 6° Año 7ma | **Grupo:** N° 2  
**Integrantes:** Elias Ramos, Erik Atusparia, Mateo Florentin, Tiziano Ciocca  

---

## Breve Descripción del Producto

Este software es un prototipo de utilidad de diagnóstico de red compatible de forma nativa con **Windows** y **Linux**. Ha sido diseñado para auditar, probar e inspeccionar servicios web HTTP/HTTPS evaluando los conceptos trabajados en el TP N°13:

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
   git clone <URL_DE_TU_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
