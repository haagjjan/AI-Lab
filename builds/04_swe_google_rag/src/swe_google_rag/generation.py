"""Format retrieved evidence and call the configured Google-hosted Gemma model.

The future API integration should reuse the proven environment validation and
model invocation pattern in ../01_mini_rag/google_api_call.py without copying
that script wholesale. The grounding prompt must require an explicit
insufficient-information response when retrieved evidence cannot answer the
question.
"""

from collections.abc import Sequence

from .config import Settings
from .schemas import RetrievedChunk


def format_retrieved_context(results: Sequence[RetrievedChunk]) -> str:
    """Format retrieved text and provenance for the generation prompt."""
    # TODO: Include stable source labels, page numbers, and chunk IDs.
    ...


def generate_grounded_answer(
    question: str,
    context: str,
    settings: Settings,
) -> str:
    """Ask the configured Gemma model to answer from retrieved context only."""
    # TODO: Build the grounding prompt, call the verified model ID, and retain
    # usage/error information needed for later evaluation.
    ...
