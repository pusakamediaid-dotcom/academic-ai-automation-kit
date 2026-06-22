import pypdf
import re

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF file path."""
    try:
        with open(file_path, "rb") as f:
            return extract_text_from_pdf_bytes(f.read())
    except Exception as e:
        raise RuntimeError(f"Failed to open PDF file: {e}")

def extract_text_from_pdf_bytes(file_bytes: bytes) -> str:
    """Extracts text from PDF bytes."""
    try:
        reader = pypdf.PdfReader(pypdf.PdfReader(pypdf.BinaryIO(file_bytes) if hasattr(pypdf, 'BinaryIO') else pypdf.PdfReader(pypdf.utils.BytesIO(file_bytes))))
        # Wait, pypdf usage is simpler:
        import io
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise RuntimeError(f"PDF extraction failed: {e}")

def clean_extracted_text(text: str) -> str:
    """Cleans extracted PDF text from common noise."""
    if not text:
        return ""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove common PDF artifacts (like page numbers or headers)
    # Note: Basic cleaning. Advanced cleaning requires regex patterns for specific journals.
    return text.strip()
