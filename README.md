# 📚 Doc Seek

**Doc Seek** es una app local para organizar, buscar y leer documentos de forma más cómoda.

La idea es simple: colocás tus archivos en una carpeta, la app los escanea y después podés buscar temas dentro de tus PDFs, TXT o archivos Markdown sin tener que abrir documento por documento.

---

## ✨ ¿Qué hace?

- Escanea documentos locales.
- Extrae texto de archivos PDF, TXT y MD.
- Permite buscar temas dentro de tus documentos.
- Muestra el párrafo relevante donde aparece lo que buscás.
- Indica la página del PDF donde está la coincidencia.
- Genera un resumen corto del documento.
- Sugiere palabras clave.
- Calcula un tiempo estimado de lectura.
- Incluye un cronómetro para medir tu velocidad real de lectura.
- Ajusta futuras estimaciones según tu promedio personal de palabras por minuto.
- Tiene interfaz en español e inglés.

---

## 🛠️ Herramientas utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-2E8B57?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

---

## 📁 Estructura del proyecto

```text
doc-seek/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── .gitkeep
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

## 🚀 Instalación

Crear un entorno virtual:

```powershell
python -m venv venv
```

Activarlo en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Ejecutar la app:

```powershell
streamlit run app.py
```

---

## 📄 Cómo usarla

1. Colocá tus archivos dentro de la carpeta `documents/`.
2. Abrí la app con Streamlit.
3. Entrá a la sección de escaneo.
4. Presioná el botón para indexar los documentos.
5. Buscá un tema o palabra clave.
6. Revisá los documentos sugeridos, las páginas y los fragmentos relevantes.
7. Usá el cronómetro si querés que la app aprenda tu velocidad de lectura.

---

## 📌 Alcance actual

Este proyecto es un MVP funcional.

Actualmente permite organizar y buscar documentos locales de manera simple, con foco en lectura, estudio y consulta rápida de información.

Está pensado para uso personal y local.

---

## ⚠️ Limitaciones

- No lee correctamente PDFs escaneados como imagen.
- No incluye OCR.
- La búsqueda usa TF-IDF, no embeddings semánticos.
- Los resúmenes son simples y extractivos.
- El almacenamiento se hace en archivos JSON locales.
- No está pensado todavía para miles de documentos.

---

## 🌱 Futuras mejoras

- Agregar OCR para PDFs escaneados.
- Mejorar la búsqueda con embeddings.
- Agregar resaltado visual de coincidencias.
- Abrir PDFs directamente en una página específica.
- Migrar de JSON a SQLite.
- Crear colecciones o etiquetas de documentos.
- Agregar historial de lectura más completo.
- Mejorar los resúmenes con modelos de lenguaje.

---

## 💡 Motivación

Doc Seek nace de una necesidad bastante cotidiana: tener muchos documentos guardados y no recordar exactamente dónde estaba una idea, frase o concepto.

La app busca reducir esa fricción y hacer que encontrar información dentro de lecturas locales sea más rápido, simple y ordenado.
