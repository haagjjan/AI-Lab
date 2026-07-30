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
    _validate_chunk_settings(
        chunk_size_tokens=chunk_size_tokens,
        chunk_overlap_tokens=chunk_overlap_tokens,
    )

    chunks: list[DocumentChunk] = []

    for page in pages:
        if not page.text.strip():
            continue

        token_ids = tokenizer.encode(
            page.text,
            add_special_tokens=False,
        )

        start = 0
        chunk_index = 0

        while start < len(token_ids):
            end = min(start + chunk_size_tokens, len(token_ids))
            chunk_token_ids = token_ids[start:end]

            chunk_text = tokenizer.decode(
                chunk_token_ids,
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            ).strip()

            if chunk_text:
                chunks.append(
                    DocumentChunk(
                        chunk_id=_create_chunk_id(
                            page=page,
                            chunk_index=chunk_index,
                            chunk_text=chunk_text,
                        ),
                        text=chunk_text,
                        source_filename=page.source_path.name,
                        page_number=page.page_number,
                        section=page.section,
                        metadata={
                            "source_path": page.source_path.as_posix(),
                            "chunk_index": chunk_index,
                            "token_start": start,
                            "token_end": end,
                            "token_count": len(chunk_token_ids),
                        },
                    )
                )

            if end == len(token_ids):
                break

            start = end - chunk_overlap_tokens
            chunk_index += 1

    return chunks



def _validate_chunk_settings(
    chunk_size_tokens: int,
    chunk_overlap_tokens: int,
) -> None:
    """Validate chunk size and overlap values."""
    if chunk_size_tokens <= 0:
        raise ValueError("chunk_size_tokens must be greater than zero.")

    if chunk_overlap_tokens < 0:
        raise ValueError("chunk_overlap_tokens must not be negative.")

    if chunk_overlap_tokens >= chunk_size_tokens:
        raise ValueError(
            "chunk_overlap_tokens must be smaller than chunk_size_tokens."
        )



def _create_chunk_id(
    page: ExtractedPage,
    chunk_index: int,
    chunk_text: str,
) -> str:
    """Create a deterministic identifier for one document chunk."""
    identity = (
        f"{page.source_path.as_posix()}\n"
        f"{page.page_number}\n"
        f"{chunk_index}\n"
        f"{chunk_text}"
    )

    digest = sha256(identity.encode("utf-8")).hexdigest()[:16]
    page_label = page.page_number if page.page_number is not None else "unknown"

    return (
        f"{page.source_path.stem}"
        f"-p{page_label}"
        f"-c{chunk_index:04d}"
        f"-{digest}"
    )