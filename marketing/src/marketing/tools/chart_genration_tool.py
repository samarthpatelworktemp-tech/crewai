from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os


class ChartToolInput(BaseModel):
    chart_type: str = Field(..., description="Type of chart: 'bar', 'line', or 'pie'")
    data: dict = Field(..., description="Dictionary of labels and values for the chart")
    title: str = Field(..., description="Title of the chart")
    filename: str = Field("chart.png", description="Optional filename for the chart (e.g., 'budget_allocation.png')")


class ChartTool(BaseTool):
    name: str = "Chart Generator Tool"
    description: str = "Generates a chart (bar, line, or pie) from given data and title"
    args_schema = ChartToolInput

    def _run(self, chart_type: str, data: dict, title: str, filename: str = "chart.png") -> str:
        labels = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(8, 5))
        plt.title(title)

        if chart_type.lower() == 'bar':
            plt.bar(labels, values, color='skyblue')
        elif chart_type.lower() == 'line':
            plt.plot(labels, values, marker='o', linestyle='-', color='green')
        elif chart_type.lower() == 'pie':
            plt.pie(values, labels=labels, autopct='%1.1f%%')
        else:
            return f"Unsupported chart type: {chart_type}"
 
        os.makedirs("charts", exist_ok=True)
        filepath = os.path.join("charts", filename)
        plt.savefig(filepath)
        plt.close()

        return f"Chart saved at: {filepath}"
