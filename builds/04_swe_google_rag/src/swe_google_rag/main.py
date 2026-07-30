"""Provide the eventual command-line entry point for indexing and questioning.

The CLI is intentionally absent at scaffold time. It should later expose clear
index and ask commands without hiding the underlying learning stages.
"""

import argparse
from pathlib import Path

from .config import load_settings
from .indexing import build_document_index
from .rag import answer_question

def main() -> None:
    """Parse CLI arguments and run the selected indexing or query operation."""
    parser = _build_parser()
    args = parser.parse_args()

    settings = load_settings(env_file=args.env_file)

    if args.command == "index":
        build_document_index(settings)
        print("Document index built successfully.")
        return

    if args.command == "ask":
        question = " ".join(args.question)

        answer = answer_question(
            question=question,
            settings=settings,
        )

        print("\nAnswer:\n")
        print(answer.text)

        print("\nRetrieved sources:\n")

        for source_number, result in enumerate(answer.sources, start=1):
            chunk = result.chunk

            page = (
                chunk.page_number
                if chunk.page_number is not None
                else "unknown"
            )

            print(
                f"[Source {source_number}] "
                f"{chunk.source_filename}, "
                f"page {page}, "
                f"score={result.similarity_score:.4f}"
            )

        return

    raise RuntimeError(f"Unsupported command: {args.command}")


def _build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="RAG over Software Engineering at Google PDFs."
    )

    parser.add_argument(
        "--env-file",
        type=Path,
        default=None,
        help="Optional path to the environment file.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    subparsers.add_parser(
        "index",
        help="Build the vector index from configured PDF files.",
    )

    ask_parser = subparsers.add_parser(
        "ask",
        help="Ask a question using the stored vector index.",
    )

    ask_parser.add_argument(
        "question",
        nargs="+",
        help="Question to answer from the indexed documents.",
    )

    return parser


if __name__ == "__main__":
    main()
