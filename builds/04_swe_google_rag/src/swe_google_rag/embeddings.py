"""Integrate the configured Google embedding model for documents and questions.

Indexing and query-time embeddings must use the same model, task-compatible
input formatting, and output dimensionality. No API calls exist in the
scaffold.
"""

from collections.abc import Sequence


from google import genai
from google.genai import types

from .config import Settings
from .schemas import DocumentChunk


def embed_document_chunks(
    chunks: Sequence[DocumentChunk],
    settings: Settings,
) -> list[list[float]]:
    """Return one embedding vector for each document chunk."""
    if not chunks:
        return []

    texts = [chunk.text for chunk in chunks]

    vectors = _embed_texts(
        texts=texts,
        task_type="RETRIEVAL_DOCUMENT",
        settings=settings,
    )

    if len(vectors) != len(chunks):
        raise RuntimeError(
            "The embedding API returned a different number of vectors "
            "than the number of document chunks."
        )

    return vectors


def embed_question(question: str, settings: Settings) -> list[float]:
    """Embed one complete short question for retrieval."""
    question = question.strip()

    if not question:
        raise ValueError("Question must not be empty.")

    vectors = _embed_texts(
        texts=[question],
        task_type="RETRIEVAL_QUERY",
        settings=settings,
    )


def _embed_texts(
    texts: Sequence[str],
    task_type: str,
    settings: Settings,
) -> list[list[float]]:
    """Request embeddings and validate their dimensions."""
    client = genai.Client(api_key=settings.google_api_key)

    response = client.models.embed_content(
        model=settings.embedding_model,
        contents=list(texts),
        config=types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=settings.embedding_dimension,
        ),
    )


    if not response.embeddings:
        raise RuntimeError("The embedding API returned no embeddings.")

    vectors: list[list[float]] = []

    for embedding in response.embeddings:
        if embedding.values is None:
            raise RuntimeError("The embedding API returned an empty vector.")

        vectors.append(list(embedding.values))

    _validate_embedding_dimensions(
        vectors=vectors,
        expected_dimension=settings.embedding_dimension,
    )

    return vectors


def _validate_embedding_dimensions(
    vectors: Sequence[Sequence[float]],
    expected_dimension: int | None,
) -> None:
    """Ensure all returned vectors have one consistent dimension."""
    if not vectors:
        raise ValueError("No vectors were provided for validation.")

    actual_dimension = len(vectors[0])

    if actual_dimension == 0:
        raise RuntimeError("The embedding API returned a zero-length vector.")

    for vector in vectors:
        if len(vector) != actual_dimension:
            raise RuntimeError(
                "The embedding API returned inconsistent vector dimensions."
            )

    if (
        expected_dimension is not None
        and actual_dimension != expected_dimension
    ):
        raise RuntimeError(
            f"Expected embedding dimension {expected_dimension}, "
            f"but received {actual_dimension}."
        )