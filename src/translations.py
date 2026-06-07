"""Translation strings for the Doc Seek interface."""

TRANSLATIONS = {
    "en": {
        "app_title": "Doc Seek",
        "app_subtitle": "Automatic organizer for local readings and documents.",
        "sidebar_hint": "Place your PDF, TXT, and MD files inside the documents folder.",
        "home_description": (
            "Scan your local documents, search topics inside them, preview PDF files, "
            "and estimate reading time using your personal reading speed."
        ),
        "documents_indexed": "Documents indexed",
        "average_wpm": "Average WPM",
        "not_calibrated": "Not calibrated",
        "documents_folder": "Documents folder",
        "tab_scan": "Scan",
        "tab_search": "Search",
        "tab_timer": "Reading timer",
        "scan_title": "Scan documents",
        "scan_description": (
            "This will scan the documents folder and index PDF, TXT, and Markdown files."
        ),
        "scan_button": "Scan documents",
        "scan_spinner": "Scanning documents...",
        "scan_success": "Documents scanned successfully.",
        "search_title": "Search documents",
        "search_input": "Search topic",
        "search_placeholder": "Example: machine learning, product strategy, Python...",
        "search_results": "Search results",
        "no_results": "No results found.",
        "score": "Score",
        "summary": "Summary",
        "keywords": "Keywords",
        "word_count": "Words",
        "estimated_time": "Estimated reading time",
        "file_path": "File path",
        "matches": "Relevant matches",
        "page": "Page",
        "match_score": "Match score",
        "not_available": "N/A",
        "pdf_preview": "PDF preview",
        "timer_title": "Reading timer",
        "timer_description": (
            "Measure how long it takes you to read a document. "
            "Doc Seek will use your historical average to estimate future reading times."
        ),
        "timer_no_documents": "Scan documents before using the timer.",
        "timer_document_select": "Document",
        "start_timer": "Start timer",
        "stop_timer": "Stop timer",
        "timer_started": "Timer started.",
        "timer_not_started": "Start the timer first.",
        "timer_saved": "Reading session saved.",
        "relevant_fragment": "Relevant fragment",
    },
    "es": {
        "app_title": "Doc Seek",
        "app_subtitle": "Organizador automático de lecturas y documentos locales.",
        "sidebar_hint": "Colocá tus archivos PDF, TXT y MD dentro de la carpeta documents.",
        "home_description": (
            "Escaneá tus documentos locales, buscá temas dentro de ellos, previsualizá PDFs "
            "y estimá tiempos de lectura usando tu velocidad personalizada."
        ),
        "documents_indexed": "Documentos indexados",
        "average_wpm": "PPM promedio",
        "not_calibrated": "Sin calibrar",
        "documents_folder": "Carpeta de documentos",
        "tab_scan": "Escanear",
        "tab_search": "Buscar",
        "tab_timer": "Cronómetro de lectura",
        "scan_title": "Escanear documentos",
        "scan_description": (
            "Esto va a escanear la carpeta documents e indexar archivos PDF, TXT y Markdown."
        ),
        "scan_button": "Escanear documentos",
        "scan_spinner": "Escaneando documentos...",
        "scan_success": "Documentos escaneados correctamente.",
        "search_title": "Buscar documentos",
        "search_input": "Tema a buscar",
        "search_placeholder": "Ejemplo: machine learning, estrategia de producto, Python...",
        "search_results": "Resultados de búsqueda",
        "no_results": "No se encontraron resultados.",
        "score": "Puntaje",
        "summary": "Resumen",
        "keywords": "Palabras clave",
        "word_count": "Palabras",
        "estimated_time": "Tiempo estimado de lectura",
        "file_path": "Ruta del archivo",
        "matches": "Coincidencias relevantes",
        "page": "Página",
        "match_score": "Puntaje de coincidencia",
        "not_available": "N/D",
        "pdf_preview": "Previsualización del PDF",
        "timer_title": "Cronómetro de lectura",
        "timer_description": (
            "Medí cuánto tardás en leer un documento. "
            "Doc Seek va a usar tu promedio histórico para estimar tiempos futuros."
        ),
        "timer_no_documents": "Escaneá documentos antes de usar el cronómetro.",
        "timer_document_select": "Documento",
        "start_timer": "Iniciar cronómetro",
        "stop_timer": "Detener cronómetro",
        "timer_started": "Cronómetro iniciado.",
        "timer_not_started": "Primero iniciá el cronómetro.",
        "timer_saved": "Sesión de lectura guardada.",
        "relevant_fragment": "Fragmento relevante",
    },
}


def get_text(language: str) -> dict:
    """Return translations for the selected language."""
    return TRANSLATIONS.get(language, TRANSLATIONS["en"])