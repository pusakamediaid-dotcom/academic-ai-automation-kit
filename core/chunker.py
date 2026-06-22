def chunk_text(text, max_chars=3000):
    """Chunks text into smaller pieces to avoid model token limits."""
    chunks = []
    for i in range(0, len(text), max_chars):
        chunks.append(text[i:i + max_chars])
    return chunks
