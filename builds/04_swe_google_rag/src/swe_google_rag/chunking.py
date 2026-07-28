"""Split extracted PDF text into overlapping, token-bounded chunks.

The tokenizer choice is intentionally deferred until the embedding model is
confirmed. Chunking must retain page and source provenance across boundaries.
"""

from collections.abc import Sequence

from .schemas import DocumentChunk, ExtractedPage


def chunk_pages(
    pages: Sequence[ExtractedPage],
    chunk_size_tokens: int,
    chunk_overlap_tokens: int,
) -> list[DocumentChunk]:
    """Create deterministic token-based chunks from extracted pages."""
    # TODO: Select a model-appropriate tokenizer and validate overlap < size.
    # TODO: Generate stable chunk IDs and preserve page/section metadata.
    ...
