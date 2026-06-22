import pytest
from core.chunker import chunk_text
from core.exporter import Exporter
from core.summarizer import AcademicSummarizer

def test_chunk_text():
    text = "A" * 4000
    chunks = chunk_text(text, max_chars=1000)
    assert len(chunks) == 4
    assert len(chunks[0]) == 1000

def test_exporter_markdown():
    md = Exporter.to_markdown("Title", "Content", "Mode")
    assert "# Title" in md
    assert "Content" in md
    assert "Mode" in md

def test_exporter_json():
    import json
    js_str = Exporter.to_json("Title", "Content", "Mode")
    data = json.loads(js_str)
    assert data["title"] == "Title"
    assert data["content"] == "Content"

def test_summarizer_fallback():
    # Testing that it doesn't crash without token
    try:
        summ = AcademicSummarizer(hf_token=None)
        # We don't run a full summary here to avoid slow tests/API limits
        assert summ.model_name == "facebook/bart-large-cnn"
    except Exception as e:
        pytest.fail(f"Summarizer failed to initialize without token: {e}")
