"""Orchestrate PDF discovery, extraction, chunking, embedding, and persistence."""

from .config import Settings


def build_document_index(settings: Settings) -> None:
    """Build and persist a local vector index from configured PDF inputs."""
    # TODO: Connect the small indexing stages and expose useful progress without
    # logging document contents, credentials, or misleading success states.
    ...
