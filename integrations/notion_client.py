import os
import requests

class NotionClient:
    def __init__(self):
        self.api_key = os.getenv("NOTION_API_KEY")
        self.database_id = os.getenv("NOTION_DATABASE_ID")
        self.version = "2022-06-28"

    def is_notion_configured(self) -> bool:
        return bool(self.api_key and self.database_id)

    def build_notion_properties(self, report_data: dict) -> dict:
        """Maps report data to Notion database properties."""
        return {
            "Title": {"title": [{"text": {"content": report_data.get("title", "Untitled Research")}}]},
            "Source Type": {"select": {"name": report_data.get("source_type", "text")}},
            "Summary": {"rich_text": [{"text": {"content": report_data.get("summary_short", "")[:2000]}}]},
            "Main Finding": {"rich_text": [{"text": {"content": report_data["key_insights"].get("main_findings", "")[:2000]}}]},
            "Research Gap": {"rich_text": [{"text": {"content": report_data["key_insights"].get("research_gap", "")[:2000]}}]},
            "Processed At": {"date": {"start": report_data.get("metadata", {}).get("processed_at", "")}},
            "PDF Report URL": {"url": report_data.get("pdf_report_url", "")}
        }

    def build_notion_children(self, report_data: dict) -> list:
        """Builds the body of the Notion page."""
        blocks = []
        
        # Short Summary
        blocks.append({"type": "heading_2", "heading_2": {"rich_text": [{"text": {"content": "Short Summary"}}]}})
        blocks.append({"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": report_data.get("summary_short", "")}}]}})
        
        # Detailed Summary
        blocks.append({"type": "heading_2", "heading_2": {"rich_text": [{"text": {"content": "Detailed Summary"}}]}})
        blocks.append({"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": report_data.get("summary_detailed", "")}}]}})
        
        # Key Insights
        blocks.append({"type": "heading_2", "heading_2": {"rich_text": [{"text": {"content": "Key Insights"}}]}})
        insights = report_data.get("key_insights", {})
        for key, value in insights.items():
            blocks.append({"type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"text": {"content": f"**{key.replace('_', ' ').title()}**: {value}"}}]}})
            
        return blocks

    def sync_to_notion_database(self, report_data: dict) -> dict:
        if not self.is_notion_configured():
            return {"ok": False, "configured": False, "message": "Notion integration not configured."}
        
        url = "https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.version,
            "Content-Type": "application/json"
        }
        
        payload = {
            "parent": {"database_id": self.database_id},
            "properties": self.build_notion_properties(report_data),
            "children": self.build_notion_children(report_data)
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                return {"ok": True, "configured": True, "url": response.json().get("url")}
            else:
                return {"ok": False, "configured": True, "message": response.text}
        except Exception as e:
            return {"ok": False, "configured": True, "message": str(e)}
