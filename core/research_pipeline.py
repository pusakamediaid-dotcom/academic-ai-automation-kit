import datetime
from core.chunker import chunk_text
from core.summarizer import AcademicSummarizer
from core.insights import InsightExtractor
from core.exporter import Exporter
from integrations.hf_client import HFClient

class ResearchPipeline:
    def __init__(self):
        self.hf_client = HFClient()
        self.exporter = Exporter()
        self.summarizer = AcademicSummarizer()
        self.extractor = InsightExtractor(self.summarizer)

    def run(self, text: str, source_type: str, mode: str = "detailed") -> dict:
        """
        The Master Pipeline: 
        Text -> Chunk -> AI Summarize -> Insights -> Export -> Structured Report
        """
        if not text or not text.strip():
            raise ValueError("Input text is empty.")

        # 1. Chunking
        chunks = chunk_text(text)
        chunk_count = len(chunks)
        word_count = len(text.split())

        # 2. AI Processing
        # Short Summary
        summary_short = self.hf_client.summarize_chunks(chunks, mode="short")
        # Detailed Summary
        summary_detailed = self.hf_client.summarize_chunks(chunks, mode="detailed")
        # Key Insights (Structured)
        # We process the summary_detailed to extract insights to avoid redundant API calls
        key_insights_text = self.extractor.extract_insights(summary_detailed)
        
        # Parsing the structured text from extractor into a dict
        key_insights_dict = self._parse_insights(key_insights_text)
        
        # Literature Review Notes
        lit_notes = self.hf_client.summarize_chunks(chunks, mode="review")

        # 3. Metadata
        metadata = {
            "processed_at": datetime.datetime.now().isoformat(),
            "model": self.hf_client.model_name,
            "chunk_count": chunk_count,
            "word_count": word_count
        }

        # 4. Reports
        markdown_report = self.exporter.to_markdown_report({
            "title": "Research Report",
            "summary_short": summary_short,
            "summary_detailed": summary_detailed,
            "key_insights": key_insights_dict,
            "literature_review_notes": lit_notes,
            "metadata": metadata
        })
        
        json_report = self.exporter.to_json_report({
            "summary_short": summary_short,
            "summary_detailed": summary_detailed,
            "key_insights": key_insights_dict,
            "literature_review_notes": lit_notes,
            "metadata": metadata
        })

        # Final Standard Output
        return {
            "title": "Research Report",
            "source_type": source_type,
            "summary_short": summary_short,
            "summary_detailed": summary_detailed,
            "key_insights": key_insights_dict,
            "literature_review_notes": lit_notes,
            "markdown_report": markdown_report,
            "json_report": json_report,
            "metadata": metadata
        }

    def _parse_insights(self, text: str) -> dict:
        """Converts the structured insight string into a dictionary."""
        insights = {}
        lines = text.split('\n')
        for line in lines:
            if line.startswith("- **Core Thesis**:"): insights["core_thesis"] = line.split(":", 1)[1].strip()
            elif line.startswith("- **Methodology**:"): insights["methodology"] = line.split(":", 1)[1].strip()
            elif line.startswith("- **Main Findings**:"): insights["main_findings"] = line.split(":", 1)[1].strip()
            elif line.startswith("- **Research Gap**:"): insights["research_gap"] = line.split(":", 1)[1].strip()
            elif line.startswith("- **Practical Implication**:"): insights["practical_implication"] = line.split(":", 1)[1].strip()
        
        # Fallbacks
        defaults = {
            "core_thesis": "Not explicitly identified.",
            "methodology": "Not explicitly identified.",
            "main_findings": "Not explicitly identified.",
            "research_gap": "Not explicitly identified.",
            "practical_implication": "Not explicitly identified."
        }
        for k, v in defaults.items():
            if k not in insights: insights[k] = v
            
        return insights
