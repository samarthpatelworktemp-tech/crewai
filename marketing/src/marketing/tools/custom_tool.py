from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from pptx import Presentation 


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


class PresentationToolInput(BaseModel):
    argument: str = Field(..., description="Input for the presentation tool.")


class PresentationTool(BaseTool):
    name: str = "Presentation Creation Tool"
    description: str = (
        "A tool to create presentations based on marketing strategies and campaign ideas."
    )
    args_schema: Type[BaseModel] = PresentationToolInput

    def _run(self, argument: str) -> str:
        """
        Create a presentation based on the provided argument.
        Format: 'topic|summary|target_audience|marketing_campaigns|campaign_1|campaign_2|campaign_3|campaign_4|campaign_5|Budget_allocation|KPIs|Conclusion'
        """
        try:
            topic, summary, target_audience, marketing_campaigns, campaign_1,campaign_2, campaign_3,campaign_4,campaign_5,Budget_allocation,KPIs,Conclusion= argument.split("|")
        except ValueError:
            return "❌ Invalid argument format. Expected format: 'topic|summary|target_audience|marketing_campaigns|campaign_1|campaign_2|campaign_3|campaign_4|campaign_5|Budget_allocation|KPIs|Conclusion'"

        return self._generate_ppt(topic.strip(), summary.strip(), target_audience.strip(),marketing_campaigns.strip(), campaign_1.strip(), campaign_2.strip(), campaign_3.strip(), campaign_4.strip(), campaign_5.strip(), Budget_allocation.strip(), KPIs.strip(), Conclusion.strip())

    def _generate_ppt(self, topic: str, summary: str, target_audience: str,marketing_campaigns:str, campaign_1:str,campaign_2:str,campaign_3:str,campaign_4:str,campaign_5:str,Budget_allocation:str,KPIs:str,Conclusion:str) -> str:

        ppt = Presentation()
        # Title Slide
        title_slide_layout = ppt.slide_layouts[0]
        slide = ppt.slides.add_slide(title_slide_layout)
        slide.shapes.title.text = f"Project Report: {topic}"

        self._add_slide(ppt, "Summary", summary)

        self._add_slide(ppt, "Tareget_audience", target_audience)
        self._add_slide(ppt, "Marketing Campaigns", marketing_campaigns)
        self._add_slide(ppt, "Campaign 1", campaign_1)
        self._add_slide(ppt, "Campaign 2", campaign_2)
        self._add_slide(ppt, "Campaign 3", campaign_3)
        self._add_slide(ppt, "Campaign 4", campaign_4)
        self._add_slide(ppt, "Campaign 5", campaign_5)
        self._add_slide(ppt, "Budget Allocation", Budget_allocation)
        self._add_slide(ppt, "KPIs", KPIs)
        self._add_slide(ppt, "Conclusion", Conclusion)

        file_path = f"{topic}_report.pptx"
        ppt.save(file_path)
        return f"✅ PPT report generated: {file_path}"

    def _add_slide(self, ppt: Presentation, title: str, content: str):
        slide_layout = ppt.slide_layouts[1]
        slide = ppt.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        textbox = slide.placeholders[1]
        textbox.text = content.strip()[:3000]
