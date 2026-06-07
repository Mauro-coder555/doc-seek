"""Document processing utilities for Doc Seek."""

from datetime import datetime
from pathlib import Path
import re
from typing import Any

import fitz
from sklearn.feature_extraction.text import TfidfVectorizer


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def scan_documents(documents_dir: Path) -> dict[str, Any]:
    """Scan supported documents and return metadata."""
    documents_dir.mkdir(exist_ok=True)

    documents = []

    for file_path in sorted(documents_dir.iterdir()):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        document = process_document(file_path)
        documents.append(document)

    return {
        "documents": documents,
        "processed_at": datetime.now().isoformat(timespec="seconds"),
    }


def process_document(file_path: Path) -> dict[str, Any]:
    """Process a single document."""
    extension = file_path.suffix.lower()

    if extension == ".pdf":
        pages = extract_pdf_pages(file_path)
        document_type = "pdf"
    elif extension in {".txt", ".md"}:
        pages = extract_text_file_pages(file_path)
        document_type = extension.replace(".", "")
    else:
        pages = []

    full_text = "\n\n".join(page["text"] for page in pages)
    paragraphs = build_paragraph_index(pages)
    word_count = count_words(full_text)

    return {
        "title": file_path.name,
        "path": str(file_path),
        "type": document_type,
        "word_count": word_count,
        "page_count": len(pages),
        "summary": summarize_text(full_text),
        "keywords": extract_keywords(full_text),
        "pages": pages,
        "paragraphs": paragraphs,
        "processed_at": datetime.now().isoformat(timespec="seconds"),
    }


def extract_pdf_pages(file_path: Path) -> list[dict[str, Any]]:
    """Extract text from a PDF, preserving page numbers."""
    pages = []

    with fitz.open(file_path) as pdf:
        for page_index, page in enumerate(pdf, start=1):
            text = page.get_text("text")
            cleaned_text = clean_text(text)

            pages.append(
                {
                    "page_number": page_index,
                    "text": cleaned_text,
                }
            )

    return pages


def extract_text_file_pages(file_path: Path) -> list[dict[str, Any]]:
    """Extract text from TXT or Markdown files."""
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    cleaned_text = clean_text(text)

    return [
        {
            "page_number": None,
            "text": cleaned_text,
        }
    ]


def build_paragraph_index(pages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Build searchable paragraph records."""
    paragraph_records = []

    for page in pages:
        raw_paragraphs = split_into_paragraphs(page["text"])

        for paragraph_index, paragraph in enumerate(raw_paragraphs, start=1):
            if len(paragraph.split()) < 5:
                continue

            paragraph_records.append(
                {
                    "page_number": page["page_number"],
                    "paragraph_index": paragraph_index,
                    "text": paragraph,
                }
            )

    return paragraph_records


def split_into_paragraphs(text: str) -> list[str]:
    """Split text into readable paragraphs."""
    blocks = re.split(r"\n\s*\n", text)
    paragraphs = []

    for block in blocks:
        cleaned_block = clean_text(block)

        if cleaned_block:
            paragraphs.append(cleaned_block)

    return paragraphs


def clean_text(text: str) -> str:
    """Normalize whitespace in extracted text."""
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def count_words(text: str) -> int:
    """Count words in text."""
    return len(re.findall(r"\b\w+\b", text))


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """Create a short extractive summary."""
    cleaned_text = clean_text(text)

    if not cleaned_text:
        return ""

    sentences = re.split(r"(?<=[.!?])\s+", cleaned_text)
    selected_sentences = sentences[:max_sentences]

    summary = " ".join(selected_sentences).strip()

    if len(summary) > 700:
        summary = summary[:700].rsplit(" ", 1)[0] + "..."

    return summary


def extract_keywords(text: str, max_keywords: int = 8) -> list[str]:
    """Extract keywords using TF-IDF."""
    cleaned_text = clean_text(text)

    if not cleaned_text or len(cleaned_text.split()) < 10:
        return []

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=50,
            ngram_range=(1, 2),
        )

        tfidf_matrix = vectorizer.fit_transform([cleaned_text])
        scores = tfidf_matrix.toarray()[0]
        terms = vectorizer.get_feature_names_out()

        ranked_terms = sorted(
            zip(terms, scores),
            key=lambda item: item[1],
            reverse=True,
        )

        keywords = [
            term for term, score in ranked_terms[:max_keywords] if score > 0
        ]

        return keywords

    except ValueError:
        return []