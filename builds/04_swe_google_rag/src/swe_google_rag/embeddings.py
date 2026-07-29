"""Integrate the configured Google embedding model for documents and questions.

Indexing and query-time embeddings must use the same model, task-compatible
input formatting, and output dimensionality. No API calls exist in the
scaffold.
"""

from collections.abc import Sequence

from .config import Settings
from .schemas import DocumentChunk


def embed_document_chunks(
    chunks: Sequence[DocumentChunk],
    settings: Settings,
) -> list[list[float]]:
    """Return one embedding vector for each document chunk."""
    # TODO: Create the Google client and request document-retrieval embeddings.
    # TODO: Batch safely, retain ordering, and validate returned dimensions.
    ...


def embed_question(question: str, settings: Settings) -> list[float]:
    """Embed one complete short question for retrieval."""
    # TODO: Request a query/question embedding using the same model and
    # dimensionality recorded by the persisted document index.
    ...
