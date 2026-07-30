"""Orchestrate query embedding, retrieval, context building, and generation."""

from .config import Settings
from .schemas import RagAnswer, RetrievedChunk


def retrieve_for_question(
    question: str,
    settings: Settings,
) -> list[RetrievedChunk]:
    """Embed one question and retrieve the configured number of chunks."""
    # TODO: Load the index, verify embedding compatibility, embed the question,
    # and delegate transparent similarity search to vector_store.
    ...


def answer_question(question: str, settings: Settings) -> RagAnswer:
    """Run the complete query-time RAG pipeline for one question."""
    # TODO: Retrieve evidence, format context, generate an answer, and attach
    # exactly the source chunks supplied to the generation model.
    ...
