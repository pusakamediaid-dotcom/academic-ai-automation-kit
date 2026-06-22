import re

def chunk_text(text, max_chars=3000):
    """Chunks text based on paragraphs and sentences to avoid cutting mid-word or mid-sentence."""
    if not text:
        return []
    
    # First, try splitting by double newlines (paragraphs)
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) + 2 <= max_chars:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            
            # If a single paragraph is larger than max_chars, split it by sentences
            if len(para) > max_chars:
                sentences = re.split(r'(?<=[.!?]) +', para)
                temp_chunk = ""
                for sentence in sentences:
                    if len(temp_chunk) + len(sentence) + 1 <= max_chars:
                        temp_chunk += sentence + " "
                    else:
                        chunks.append(temp_chunk.strip())
                        temp_chunk = sentence + " "
                current_chunk = temp_chunk
            else:
                current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks
