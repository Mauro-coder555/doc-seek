"""Search utilities for Doc Seek."""

from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def search_documents(
    metadata: dict[str, Any],
    query: str,
    max_documents: int = 10,
    max_matches_per_document: int = 10,
) -> list[dict[str, Any]]:
    """Search documents and return ranked results with paragraph matches."""
    documents = metadata.get("documents", [])

    if not documents or not query.strip():
        return []

    document_results = []

    for document in documents:
        matches = search_paragraphs(document, query, max_matches_per_document)

        if not matches:
            continue

        score = sum(match["score"] for match in matches)

        document_results.append(
            {
                "document": document,
                "score": score,
                "matches": matches,
            }
        )

    document_results.sort(key=lambda result: result["score"], reverse=True)

    return document_results[:max_documents]


def search_paragraphs(
    document: dict[str, Any],
    query: str,
    max_matches: int,
) -> list[dict[str, Any]]:
    """Search paragraphs within a single document."""
    paragraphs = document.get("paragraphs", [])

    if not paragraphs:
        return []

    paragraph_texts = [paragraph["text"] for paragraph in paragraphs]
    corpus = paragraph_texts + [query]

    try:
        vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
        )

        tfidf_matrix = vectorizer.fit_transform(corpus)

    except ValueError:
        return []

    paragraph_vectors = tfidf_matrix[:-1]
    query_vector = tfidf_matrix[-1]

    similarities = cosine_similarity(paragraph_vectors, query_vector).flatten()

    ranked_matches = []

    for index, score in enumerate(similarities):
        if score <= 0:
            continue

        paragraph = paragraphs[index]

        ranked_matches.append(
            {
                "page_number": paragraph.get("page_number"),
                "paragraph_index": paragraph.get("paragraph_index"),
                "paragraph": paragraph.get("text", ""),
                "score": float(score),
            }
        )

    ranked_matches.sort(key=lambda match: match["score"], reverse=True)

    return ranked_matches[:max_matches]