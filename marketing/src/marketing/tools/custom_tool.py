from crewai.tools import BaseTool
from typing import Type, Literal
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
    argument: str = Field(..., description="Format: 'topic|summary|tasks'")


class PresentationTool(BaseTool):
    name: str = "Presentation Creation Tool"
    description: str = (
        "A tool to create presentations based on marketing strategies and campaign ideas."
    )
    args_schema: Type[BaseModel] = PresentationToolInput

    def _run(self, argument: str) -> str:
        """
        Create a presentation based on the provided argument.
        Format: 'topic|summary|tasks'
        """
        try:
            topic, summary, tasks = argument.split("|")
        except ValueError:
            return "❌ Invalid argument format. Expected format: 'topic|summary|tasks'"

        return self._generate_ppt(topic.strip(), summary.strip(), tasks.strip())

    def _generate_ppt(self, topic: str, summary: str, tasks: str) -> str:
        ppt = Presentation()

        # Title Slide
        title_slide_layout = ppt.slide_layouts[0]
        slide = ppt.slides.add_slide(title_slide_layout)
        slide.shapes.title.text = f"Project Report: {topic}"

        self._add_slide(ppt, "Summary", summary)

        self._add_slide(ppt, "Task Plan", tasks)

        file_path = f"{topic}_report.pptx"
        ppt.save(file_path)
        return f"✅ PPT report generated: {file_path}"

    def _add_slide(self, ppt: Presentation, title: str, content: str):
        slide_layout = ppt.slide_layouts[1]
        slide = ppt.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        textbox = slide.placeholders[1]
        textbox.text = content.strip()[:3000]
