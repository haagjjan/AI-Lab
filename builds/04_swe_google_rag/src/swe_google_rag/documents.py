"""Discover PDF inputs and extract page-aware text from each document.

PDF discovery and extraction stay together because they form one small input
boundary. The eventual extractor should preserve filename and page provenance
and record section information only when it can be detected reliably.
"""


from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from .schemas import ExtractedPage


def discover_pdf_files(storage_path: Path) -> list[Path]:
    """Return PDF files found recursively in deterministic order.

    Args:
        storage_path: Root folder containing input PDF documents.

    Returns:
        A list of PDF paths sorted by their relative path.

    Raises:
        FileNotFoundError: If the configured storage path does not exist.
        NotADirectoryError: If the configured storage path is not a directory.
    """
    storage_path = storage_path.expanduser()

    #Edge cases: empty path, no dir, 

    if not storage_path.exists():
        raise FileNotFoundError(f"File not found at: {storage_path}")

    if not storage_path.is_dir():
        raise NotADirectoryError(f"PDF storage directory at: {storage_path} is no directory: " )

    pdf_files = [
        path
        for path in storage_path.rglob("*")
        if path.is_file() and path.suffix.casefold() == ".pdf"
    ]

    return sorted(
        pdf_files,
        key=lambda path: path.relative_to(storage_path).as_posix().casefold(),
    )



def extract_pdf_pages(pdf_path: Path) -> list[ExtractedPage]:
    """Extract text and page provenance from every page of one PDF.

    Empty pages are retained with an empty string. This function does not
    perform OCR or infer document sections.

    Args:
        pdf_path: Path to one PDF file.

    Returns:
        One ExtractedPage object for every physical PDF page.

    Raises:
        FileNotFoundError: If the PDF path does not exist.
        ValueError: If the path is not a PDF or the PDF is encrypted.
        PdfReadError: If pypdf cannot parse the PDF.
        RuntimeError: If text extraction fails for a specific page.
    """
