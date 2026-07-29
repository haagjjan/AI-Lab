"""Load and validate environment-based configuration for the RAG project.

The future implementation will resolve project-relative paths, validate model
selection, parse numeric settings, and avoid exposing the Google API key.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    """Configuration shared by indexing and query-time pipelines."""

    google_api_key: str
    generation_model: str
    embedding_model: str
    embedding_dimension: int | None
    pdf_storage_path: Path
    vector_store_path: Path
    chunk_size_tokens: int
    chunk_overlap_tokens: int
    top_k: int


def load_settings(env_file: Path | None = None) -> Settings:
    """Load validated settings from the environment and optional env file."""
    # TODO: Reuse the proven project-relative .env loading and missing-key
    # validation pattern from ../01_mini_rag/google_api_call.py.
    # TODO: Validate model IDs, numeric ranges, and path resolution.
    ...
