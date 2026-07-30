"""Persist chunk vectors locally and perform nearest-neighbour retrieval.

The first implementation should remain transparent and file-backed, using
NumPy and cosine similarity before considering a dedicated vector database.
"""

from collections.abc import Sequence
from pathlib import Path

from .schemas import DocumentChunk, RetrievedChunk


def save_index(
    storage_path: Path,
    chunks: Sequence[DocumentChunk],
    embeddings: Sequence[Sequence[float]],
    embedding_model: str,
    embedding_dimension: int,
) -> None:
    """Persist vectors, chunk metadata, and embedding configuration locally."""
    # TODO: Validate one-to-one chunk/vector alignment and write atomically.
    ...


def load_index(
    storage_path: Path,
) -> tuple[list[DocumentChunk], list[list[float]], str, int]:
    """Load chunks, vectors, model ID, and vector dimension from local storage."""
    # TODO: Fail clearly for a missing, corrupt, or incompatible index.
    ...


def search_index(
    chunks: Sequence[DocumentChunk],
    embeddings: Sequence[Sequence[float]],
    query_vector: Sequence[float],
    top_k: int,
) -> list[RetrievedChunk]:
    """Return the highest-similarity chunks for one query vector."""
    # TODO: Validate dimensions, compute cosine similarity, and return results
    # in descending score order with deterministic tie handling.
    ...
