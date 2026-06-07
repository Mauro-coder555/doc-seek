"""Main Streamlit application for Doc Seek."""

from pathlib import Path
import time

import streamlit as st

from src.database import (
    ensure_data_files,
    load_metadata,
    save_metadata,
    load_reading_stats,
    save_reading_stats,
)
from src.processor import scan_documents
from src.search import search_documents
from src.reading_time import (
    estimate_reading_minutes,
    add_reading_session,
    get_average_wpm,
)
from src.translations import get_text


DOCUMENTS_DIR = Path("documents")


def configure_page() -> None:
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="Doc Seek",
        page_icon="📚",
        layout="wide",
    )


def render_pdf_preview(file_path: str) -> None:
    """Render a PDF preview inside Streamlit."""
    path = Path(file_path)

    if not path.exists() or path.suffix.lower() != ".pdf":
        return

    st.iframe(
        src=path,
        height=720,
    )


def render_sidebar(text: dict) -> str:
    """Render sidebar controls and return selected language."""
    st.sidebar.title("Doc Seek")

    language_options = {
        "Español": "es",
        "English": "en",
    }

    selected_language_label = st.sidebar.selectbox(
        "Language / Idioma",
        options=list(language_options.keys()),
    )

    st.sidebar.divider()
    st.sidebar.caption(text["sidebar_hint"])

    return language_options[selected_language_label]


def render_home(text: dict, metadata: dict, reading_stats: dict) -> None:
    """Render the home dashboard."""
    documents = metadata.get("documents", [])
    average_wpm = get_average_wpm(reading_stats)

    st.title(text["app_title"])
    st.subheader(text["app_subtitle"])

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(text["documents_indexed"], len(documents))

    with col2:
        if average_wpm:
            st.metric(text["average_wpm"], round(average_wpm, 2))
        else:
            st.metric(text["average_wpm"], text["not_calibrated"])

    with col3:
        st.metric(text["documents_folder"], str(DOCUMENTS_DIR))

    st.info(text["home_description"])


def render_scan_section(text: dict) -> None:
    """Render document scanning section."""
    st.header(text["scan_title"])
    st.write(text["scan_description"])

    if st.button(text["scan_button"], type="primary"):
        with st.spinner(text["scan_spinner"]):
            metadata = scan_documents(DOCUMENTS_DIR)
            save_metadata(metadata)

        st.success(text["scan_success"])
        st.rerun()


def render_search_section(text: dict, metadata: dict, reading_stats: dict) -> None:
    """Render search interface and results."""
    st.header(text["search_title"])

    query = st.text_input(
        text["search_input"],
        placeholder=text["search_placeholder"],
    )

    if not query:
        return

    results = search_documents(metadata, query)

    if not results:
        st.warning(text["no_results"])
        return

    st.subheader(text["search_results"])

    for index, result in enumerate(results, start=1):
        document = result["document"]
        matches = result["matches"]
        word_count = document.get("word_count", 0)
        average_wpm = get_average_wpm(reading_stats)
        estimated_minutes = estimate_reading_minutes(word_count, average_wpm)

        with st.expander(
            f"{index}. {document['title']} — {text['score']}: {result['score']:.2f}",
            expanded=index == 1,
        ):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.write(f"**{text['summary']}:** {document.get('summary', '')}")
                st.write(f"**{text['keywords']}:** {', '.join(document.get('keywords', []))}")

            with col2:
                st.metric(text["word_count"], word_count)
                st.metric(text["estimated_time"], f"{estimated_minutes} min")

            st.write(f"**{text['file_path']}:** `{document['path']}`")

            st.subheader(text["matches"])

            for match in matches[:8]:
                page_label = match.get("page_number", text["not_available"])

                st.markdown(f"**{text['page']}:** {page_label}")
                st.markdown(f"**{text['relevant_fragment']}**")
                st.write(match["paragraph"])
                st.divider()

            if document["type"] == "pdf":
                st.subheader(text["pdf_preview"])
                render_pdf_preview(document["path"])


def render_reading_timer(text: dict, metadata: dict, reading_stats: dict) -> None:
    """Render reading timer controls."""
    st.header(text["timer_title"])
    st.write(text["timer_description"])

    documents = metadata.get("documents", [])

    if not documents:
        st.warning(text["timer_no_documents"])
        return

    document_titles = [document["title"] for document in documents]
    selected_title = st.selectbox(text["timer_document_select"], document_titles)

    selected_document = next(
        document for document in documents if document["title"] == selected_title
    )

    if "reading_timer_start" not in st.session_state:
        st.session_state.reading_timer_start = None

    col1, col2 = st.columns(2)

    with col1:
        if st.button(text["start_timer"]):
            st.session_state.reading_timer_start = time.time()
            st.success(text["timer_started"])

    with col2:
        if st.button(text["stop_timer"]):
            if st.session_state.reading_timer_start is None:
                st.warning(text["timer_not_started"])
            else:
                elapsed_seconds = time.time() - st.session_state.reading_timer_start
                st.session_state.reading_timer_start = None

                updated_stats = add_reading_session(
                    stats=reading_stats,
                    document_title=selected_document["title"],
                    word_count=selected_document.get("word_count", 0),
                    elapsed_seconds=elapsed_seconds,
                )

                save_reading_stats(updated_stats)

                st.success(text["timer_saved"])
                st.rerun()


def main() -> None:
    """Run the Streamlit application."""
    configure_page()
    ensure_data_files()

    raw_text = get_text("es")
    language = render_sidebar(raw_text)
    text = get_text(language)

    metadata = load_metadata()
    reading_stats = load_reading_stats()

    render_home(text, metadata, reading_stats)

    tab_scan, tab_search, tab_timer = st.tabs(
        [
            text["tab_scan"],
            text["tab_search"],
            text["tab_timer"],
        ]
    )

    with tab_scan:
        render_scan_section(text)

    with tab_search:
        render_search_section(text, metadata, reading_stats)

    with tab_timer:
        render_reading_timer(text, metadata, reading_stats)


if __name__ == "__main__":
    main()