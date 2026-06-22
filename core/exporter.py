import json

class Exporter:
    def to_markdown_report(self, report_data: dict) -> str:
        """Generates a clean, professional markdown report."""
        title = report_data.get("title", "Research Automation Report")
        short_sum = report_data.get("summary_short", "N/A")
        detailed_sum = report_data.get("summary_detailed", "N/A")
        insights = report_data.get("key_insights", {})
        lit_notes = report_data.get("literature_review_notes", "N/A")
        meta = report_data.get("metadata", {})

        md = f"# {title}\n\n"
        md += "## 📄 Short Summary\n" + short_sum + "\n\n"
        md += "## 🔍 Detailed Summary\n" + detailed_sum + "\n\n"
        md += "## 📌 Key Insights\n"
        md += f"- **Core Thesis**: {insights.get('core_thesis', 'N/A')}\n"
        md += f"- **Methodology**: {insights.get('methodology', 'N/A')}\n"
        md += f"- **Main Findings**: {insights.get('main_findings', 'N/A')}\n"
        md += f"- **Research Gap**: {insights.get('research_gap', 'N/A')}\n"
        md += f"- **Practical Implication**: {insights.get('practical_implication', 'N/A')}\n\n"
        md += "## 📚 Literature Review Notes\n" + lit_notes + "\n\n"
        md += "## ⚙️ Metadata\n"
        md += f"- **Model**: {meta.get('model', 'N/A')}\n"
        md += f"- **Processed At**: {meta.get('processed_at', 'N/A')}\n"
        md += f"- **Chunk Count**: {meta.get('chunk_count', 'N/A')}\n"
        md += f"- **Word Count**: {meta.get('word_count', 'N/A')}\n"
        
        return md

    def to_json_report(self, report_data: dict) -> str:
        return json.dumps(report_data, indent=4)

    def to_notion_blocks(self, report_data: dict) -> list:
        """Cuts report data into Notion block format."""
        # This logic is now handled by NotionClient to keep integration cohesive.
        return []

    def to_pdfmonkey_payload(self, report_data: dict) -> dict:
        """Prepares the data payload for PDFMonkey."""
        # Handled by PDFMonkeyClient for better encapsulation.
        return {}
