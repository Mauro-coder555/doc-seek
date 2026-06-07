# Doc Seek

Doc Seek es un organizador automático de lecturas y documentos locales.

La aplicación permite escanear una carpeta con archivos PDF, TXT y Markdown, extraer texto, generar palabras clave, crear resúmenes cortos, estimar tiempos de lectura y buscar temas dentro de los documentos.

## Objetivo del proyecto

El objetivo es construir una herramienta local para organizar documentos de lectura, encontrar rápidamente información relevante y mejorar las estimaciones de tiempo de lectura usando datos personalizados del usuario.

## Funcionalidades previstas

- Escaneo de documentos locales.
- Soporte para archivos PDF, TXT y Markdown.
- Extracción de texto por documento.
- Extracción de texto por página en PDFs.
- Generación de palabras clave usando TF-IDF.
- Resumen corto por documento.
- Buscador de temas.
- Visualización de documentos relevantes.
- Coincidencias por página y párrafo.
- Estimación de tiempo de lectura.
- Cronómetro integrado para medir sesiones de lectura.
- Cálculo personalizado de velocidad de lectura en palabras por minuto.
- Interfaz bilingüe en español e inglés.

## Stack técnico

- Python
- Streamlit
- PyMuPDF
- scikit-learn
- JSON local como almacenamiento inicial

## Instalación

Crear y activar el entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1