# Doc Seek

Doc Seek es un organizador automático de lecturas y documentos locales construido con Python y Streamlit.

La aplicación permite escanear una carpeta local con archivos PDF, TXT y Markdown, extraer texto, generar palabras clave, crear resúmenes cortos, estimar tiempos de lectura y buscar temas dentro de los documentos. También incluye un cronómetro para medir sesiones reales de lectura y personalizar futuras estimaciones según la velocidad promedio del usuario en palabras por minuto.

---

## Índice

1. [Descripción general](#descripción-general)
2. [Alcance del proyecto](#alcance-del-proyecto)
3. [Estructura del proyecto](#estructura-del-proyecto)
4. [Componentes principales](#componentes-principales)
5. [Herramientas y librerías utilizadas](#herramientas-y-librerías-utilizadas)
6. [Instalación](#instalación)
7. [Uso de la aplicación](#uso-de-la-aplicación)
8. [Flujo de trabajo recomendado](#flujo-de-trabajo-recomendado)
9. [Datos locales](#datos-locales)
10. [Limitaciones actuales](#limitaciones-actuales)
11. [Futuras mejoras](#futuras-mejoras)
12. [Comandos útiles de Git](#comandos-útiles-de-git)
13. [Estado actual del proyecto](#estado-actual-del-proyecto)

---

## Descripción general

Doc Seek está pensado como una herramienta local para organizar lecturas, documentos de estudio, papers, apuntes, libros técnicos, notas y archivos de referencia.

El objetivo principal es permitir que el usuario pueda:

- Cargar documentos en una carpeta local.
- Escanearlos desde una interfaz web simple.
- Buscar temas dentro de los documentos.
- Ver qué archivo contiene la información buscada.
- Identificar la página y el párrafo donde aparece la coincidencia.
- Previsualizar archivos PDF desde la interfaz.
- Calcular un tiempo estimado de lectura.
- Medir sesiones reales de lectura con un cronómetro.
- Personalizar la estimación de lectura usando el promedio histórico del usuario.

La aplicación funciona localmente y guarda sus datos en archivos JSON dentro del proyecto.

---

## Alcance del proyecto

El alcance actual corresponde a un MVP funcional.

### Incluido en el MVP

- Interfaz web con Streamlit.
- Selector de idioma entre español e inglés.
- Escaneo de documentos locales.
- Soporte para archivos PDF, TXT y Markdown.
- Extracción de texto desde PDFs usando PyMuPDF.
- Extracción de texto por página en archivos PDF.
- Separación del contenido en párrafos buscables.
- Generación de resumen corto.
- Generación de palabras clave usando TF-IDF.
- Búsqueda por tema usando similitud TF-IDF.
- Ranking interno de resultados relevantes.
- Visualización de coincidencias por documento, página y fragmento.
- Previsualización básica de PDFs.
- Cálculo de tiempo estimado de lectura.
- Cronómetro para registrar sesiones reales de lectura.
- Cálculo de velocidad promedio en palabras por minuto.
- Persistencia local en JSON.

### No incluido todavía

- OCR para PDFs escaneados como imagen.
- Base de datos relacional.
- Autenticación de usuarios.
- Sincronización en la nube.
- Indexación incremental avanzada.
- Detección automática de idioma para stopwords.
- Resúmenes con modelos de lenguaje.
- Búsqueda semántica con embeddings.

---

## Estructura del proyecto

```text
doc-seek/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── .gitkeep
│   ├── metadata.json
│   └── reading_stats.json
│
├── documents/
│   └── .gitkeep
│
└── src/
    ├── __init__.py
    ├── processor.py
    ├── search.py
    ├── database.py
    ├── reading_time.py
    └── translations.py
```

---

## Componentes principales

### `app.py`

Archivo principal de la aplicación.

Responsabilidades:

- Configurar la página de Streamlit.
- Renderizar la interfaz.
- Mostrar el dashboard principal.
- Permitir escanear documentos.
- Permitir buscar temas.
- Mostrar resultados relevantes.
- Mostrar preview de PDFs.
- Gestionar el cronómetro de lectura.
- Conectar la UI con los módulos internos.

---

### `src/processor.py`

Contiene la lógica de procesamiento de documentos.

Responsabilidades:

- Escanear la carpeta `documents/`.
- Detectar archivos soportados.
- Procesar PDFs, TXT y Markdown.
- Extraer texto por página en PDFs.
- Limpiar texto extraído.
- Dividir texto en párrafos.
- Calcular cantidad de palabras.
- Generar resumen corto.
- Generar palabras clave con TF-IDF.
- Construir la metadata base de cada documento.

---

### `src/search.py`

Contiene la lógica de búsqueda.

Responsabilidades:

- Buscar una consulta dentro de los documentos indexados.
- Comparar la consulta contra los párrafos del documento.
- Calcular similitud usando TF-IDF.
- Ordenar documentos según relevancia.
- Devolver coincidencias con página, párrafo y puntaje interno.

Nota: el puntaje de coincidencia se usa internamente para ordenar resultados. No necesariamente debe mostrarse al usuario final.

---

### `src/database.py`

Contiene la capa de persistencia local.

Responsabilidades:

- Crear archivos JSON si no existen.
- Leer `data/metadata.json`.
- Escribir `data/metadata.json`.
- Leer `data/reading_stats.json`.
- Escribir `data/reading_stats.json`.
- Manejar archivos vacíos o JSON inválidos de forma segura.

---

### `src/reading_time.py`

Contiene la lógica de estimación de lectura.

Responsabilidades:

- Calcular tiempo estimado de lectura.
- Usar una velocidad base de lectura cuando no hay historial.
- Registrar sesiones de lectura.
- Calcular la velocidad promedio del usuario en palabras por minuto.
- Actualizar estadísticas históricas.

---

### `src/translations.py`

Contiene los textos de la interfaz.

Responsabilidades:

- Centralizar las traducciones.
- Permitir una UI bilingüe.
- Evitar textos hardcodeados en `app.py`.
- Facilitar futuras traducciones.

---

### `documents/`

Carpeta donde el usuario coloca sus archivos locales.

Soporta actualmente:

- `.pdf`
- `.txt`
- `.md`

Los archivos dentro de esta carpeta están ignorados por Git para evitar subir documentos personales o pesados al repositorio.

---

### `data/`

Carpeta donde la aplicación guarda información local generada.

Archivos principales:

```text
metadata.json
reading_stats.json
```

Estos archivos están ignorados por Git porque contienen datos locales del usuario.

---

## Herramientas y librerías utilizadas

### Python

Lenguaje principal del proyecto.

### Streamlit

Framework utilizado para construir la interfaz web local.

Uso principal:

- Layout de la aplicación.
- Sidebar.
- Tabs.
- Inputs de búsqueda.
- Métricas.
- Botones.
- Visualización de resultados.

### PyMuPDF

Librería utilizada para leer archivos PDF y extraer texto por página.

Paquete usado:

```text
pymupdf
```

Import principal en código:

```python
import fitz
```

### scikit-learn

Librería utilizada para TF-IDF y cálculo de similitud.

Uso principal:

- Extracción de palabras clave.
- Vectorización de consultas y párrafos.
- Cálculo de similitud coseno.

### NumPy

Dependencia de soporte para procesamiento numérico.

### Pandas

Incluida como herramienta de soporte para posibles vistas tabulares y mejoras futuras.

### Markdown

Incluida para soporte futuro de procesamiento o conversión de archivos Markdown.

### JSON local

Sistema de almacenamiento inicial.

Ventajas:

- Simple.
- Local.
- Fácil de inspeccionar.
- Suficiente para un MVP.

---

## Instalación

Desde la carpeta raíz del proyecto:

```powershell
python -m venv venv
```

Activar el entorno virtual en PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación del entorno virtual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Luego volver a activar:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

---

## Uso de la aplicación

Colocar documentos dentro de:

```text
documents/
```

Ejecutar la aplicación:

```powershell
streamlit run app.py
```

Streamlit mostrará una URL local similar a:

```text
http://localhost:8501
```

Abrir esa URL en el navegador.

---

## Flujo de trabajo recomendado

1. Colocar PDFs, TXT o MD dentro de `documents/`.
2. Ejecutar la aplicación con `streamlit run app.py`.
3. Ir a la pestaña de escaneo.
4. Presionar el botón para escanear documentos.
5. Ir a la pestaña de búsqueda.
6. Escribir un tema o concepto.
7. Revisar los documentos sugeridos.
8. Leer los fragmentos relevantes.
9. Abrir o previsualizar el PDF si corresponde.
10. Usar el cronómetro para medir una sesión de lectura.
11. Permitir que la app actualice el promedio personalizado de palabras por minuto.

---

## Datos locales

La aplicación genera datos en:

```text
data/metadata.json
data/reading_stats.json
```

### `metadata.json`

Guarda información procesada de documentos:

- título
- ruta
- tipo de archivo
- cantidad de palabras
- cantidad de páginas
- resumen
- palabras clave
- páginas
- párrafos indexados
- fecha de procesamiento

### `reading_stats.json`

Guarda información de lectura:

- sesiones de lectura
- documento leído
- cantidad de palabras
- tiempo transcurrido
- palabras por minuto de la sesión
- promedio histórico de palabras por minuto

Estos archivos no se suben al repositorio porque son datos locales del usuario.

---

## Limitaciones actuales

### PDFs escaneados

La app extrae texto real del PDF. Si el PDF es una imagen escaneada, probablemente no encontrará contenido.

Para resolver esto sería necesario agregar OCR.

### Calidad del resumen

El resumen actual es extractivo y simple. Usa las primeras oraciones del texto, no un modelo avanzado de resumen.

### Palabras clave

Las palabras clave se generan con TF-IDF ligero. Esto es suficiente para un MVP, pero puede ser limitado en documentos largos, técnicos o en español.

### Búsqueda semántica

La búsqueda actual se basa en TF-IDF, no en embeddings. Esto significa que funciona mejor cuando la consulta comparte palabras con el texto.

Por ejemplo, puede encontrar bien:

```text
productividad
```

si el documento contiene esa palabra.

Pero puede fallar si se busca:

```text
cómo trabajar mejor
```

y el documento usa otras palabras relacionadas sin coincidencia directa.

### Idiomas

La interfaz soporta español e inglés, pero el procesamiento NLP no detecta automáticamente el idioma del documento.

### Escalabilidad

El almacenamiento JSON es simple y adecuado para un MVP. Para miles de documentos o archivos muy grandes, convendría migrar a SQLite o una base vectorial.

### Seguridad

La aplicación está pensada para uso local. No incluye autenticación, permisos ni separación de usuarios.

---

## Futuras mejoras

### OCR para PDFs escaneados

Agregar soporte con herramientas como:

- Tesseract OCR
- EasyOCR
- PyMuPDF combinado con extracción de imágenes

Esto permitiría indexar libros o papers escaneados.

### Base de datos SQLite

Migrar de JSON a SQLite para:

- Mejor rendimiento.
- Consultas más flexibles.
- Mejor integridad de datos.
- Manejo más robusto de documentos grandes.

### Búsqueda semántica

Agregar embeddings para mejorar la búsqueda conceptual.

Opciones posibles:

- sentence-transformers
- ChromaDB
- FAISS
- OpenAI embeddings
- SQLite con extensiones vectoriales

### Mejor preview de resultados

Agregar:

- Highlights sobre la palabra buscada.
- Agrupación por página.
- Botón para abrir el PDF directamente en una página específica.
- Mejor separación visual de fragmentos.

### Resúmenes avanzados

Agregar resúmenes más inteligentes usando:

- modelos locales
- APIs externas
- técnicas extractivas más elaboradas

### Mejor extracción de keywords en español

Agregar stopwords en español y detección de idioma.

### Indexación incremental

Evitar reprocesar todos los documentos cada vez.

La app podría comparar:

- ruta
- fecha de modificación
- tamaño del archivo
- hash del archivo

y procesar solo archivos nuevos o modificados.

### Etiquetas y colecciones

Permitir organizar documentos por:

- tema
- curso
- autor
- tipo de lectura
- prioridad
- estado de lectura

### Historial de lectura

Agregar dashboard con:

- documentos leídos
- tiempo total leído
- velocidad promedio por tipo de documento
- evolución del PPM
- metas de lectura

### Exportación

Permitir exportar resultados a:

- CSV
- Markdown
- JSON
- PDF

---

## Comandos útiles de Git

Inicializar repositorio:

```powershell
git init
```

Ver estado:

```powershell
git status
```

Agregar cambios:

```powershell
git add .
```

Crear commit:

```powershell
git commit -m "Build document search MVP with bilingual UI and reading timer"
```

Commit sugerido para mejoras de visualización de resultados:

```powershell
git commit -m "Improve search result readability"
```

Commit sugerido para reemplazo de componentes deprecados:

```powershell
git commit -m "Replace deprecated PDF preview component"
```

---

## Estado actual del proyecto

El proyecto ya cuenta con un MVP funcional.

Actualmente permite:

- Escanear documentos locales.
- Extraer texto de PDF, TXT y Markdown.
- Buscar temas dentro de documentos.
- Ver fragmentos relevantes.
- Identificar páginas relevantes en PDFs.
- Previsualizar PDFs.
- Estimar tiempo de lectura.
- Registrar sesiones de lectura.
- Calcular velocidad personalizada de lectura.
- Usar la interfaz en español o inglés.

---

## Próximo paso recomendado

Antes de seguir agregando features, conviene hacer una pequeña etapa de limpieza:

1. Ocultar el puntaje de coincidencia al usuario final.
2. Mejorar la visualización de fragmentos relevantes.
3. Reemplazar cualquier uso de componentes deprecados por alternativas actuales de Streamlit.
4. Validar que `git status` no incluya documentos personales ni archivos JSON locales.
5. Crear un commit estable del MVP.

Commit recomendado:

```powershell
git add . && git commit -m "Stabilize document search MVP"
```
