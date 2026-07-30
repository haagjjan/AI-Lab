"""Split extracted PDF text into overlapping, token-bounded chunks.

The tokenizer choice is intentionally deferred until the embedding model is
confirmed. Chunking must retain page and source provenance across boundaries.
"""

from collections.abc import Sequence
from hashlib import sha256

from transformers import AutoTokenizer, PreTrainedTokenizerBase

from .schemas import DocumentChunk, ExtractedPage


def load_tokenizer(model_name: str) -> PreTrainedTokenizerBase:
    """Load a local Hugging Face tokenizer.

    Args:
        model_name: Hugging Face model identifier containing tokenizer files.

    Returns:
        The tokenizer associated with the configured model.

    Raises:
        ValueError: If no tokenizer model name was provided.
    """
    model_name = model_name.strip()

    if not model_name:
        raise ValueError("TOKENIZER_MODEL must not be empty.")

    return AutoTokenizer.from_pretrained(
        model_name,
        use_fast=True,
    )

def chunk_pages(
    pages: Sequence[ExtractedPage],
    chunk_size_tokens: int,
    chunk_overlap_tokens: int,
) -> list[DocumentChunk]:
    """Create deterministic token-based chunks from extracted PDF pages.

    Each page is chunked independently so every chunk retains one exact page
    number. Empty pages are ignored.

    Args:
        pages: Extracted PDF pages in deterministic order.
        tokenizer: Local tokenizer used to encode and decode text.
        chunk_size_tokens: Maximum number of tokens per chunk.
        chunk_overlap_tokens: Tokens repeated between adjacent chunks.

    Returns:
        Document chunks in page and chunk order.

    Raises:
        ValueError: If the chunk settings are invalid.
    """
    # TODO: Select a model-appropriate tokenizer and validate overlap < size.
    # TODO: Generate stable chunk IDs and preserve page/section metadata.
    ...
