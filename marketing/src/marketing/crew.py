from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from marketing.tools.chart_genration_tool import ChartTool
from marketing.tools.custom_tool import PresentationTool
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field  


class MarketStrategy(BaseModel):
    name: str = Field(..., description="Name of the market strategy")
    tatics: List[str] = Field(..., description="List of tactics to be used in the market strategy")
    channels: List[str] = Field(..., description="List of channels to be used in the market strategy")
    KPIs: List[str] = Field(..., description="List of KPIs to be used in the market strategy")

class CampaignIdea(BaseModel):
    name: str = Field(..., description="Name of the campaign idea")
    description: str = Field(..., description="Description of the campaign idea")
    audience: str = Field(..., description="Audience of the campaign idea")
    channel: str = Field(..., description="Channel of the campaign idea")

class Copy(BaseModel):
    title: str = Field(..., description="Title of the copy")
    body: str = Field(..., description="Body of the copy")

@CrewBase
class MarketingPostsCrew():
    """MarketingPosts crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def lead_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_market_analyst'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            memory=False,
        )

    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_marketing_strategist'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            memory=False,
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator'],
            verbose=True,
            memory=False,
        )
    @agent
    def chief_creative_director(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_creative_director'],
            verbose=True,
            memory=False,
        )
    
    @agent
    def data_visualization_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['data_visualization_expert'],
            verbose=True,
            memory=False,
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.lead_market_analyst()
        )


    @task
    def project_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_understanding_task'],
            agent=self.chief_marketing_strategist()
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_strategy_task'],
            agent=self.chief_marketing_strategist()
        )

    @task
    def campaign_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['campaign_idea_task'],
            agent=self.creative_content_creator()
        )

    @task
    def copy_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['copy_creation_task'],
            agent=self.creative_content_creator(),
            context=[self.marketing_strategy_task(), self.campaign_idea_task()],
        )

    @task 
    def charts_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['charts_data_task'],
            agent=self.data_visualization_expert(),
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            context=[self.marketing_strategy_task(), self.campaign_idea_task(), self.copy_creation_task()],
        )


    @task
    def charts_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['charts_generation_task'],
            agent=self.data_visualization_expert(),
            tools=[ChartTool()],
            context=[self.charts_data_task()],
            output_format='png'  
        )
    
    @task
    def presentation_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['presentation_creation_task'],
            agent=self.chief_creative_director(),
            context=[self.marketing_strategy_task(), self.campaign_idea_task(), self.copy_creation_task(),self.charts_data_task()],
            output_format='pptx'
        )
    
    @task
    def save_presentation_task(self) -> Task:
        return Task(
            config=self.tasks_config['save_presentation_task'],
            agent=self.chief_creative_director(),
            tools=[PresentationTool()],
            context=[self.presentation_creation_task()],
        )
   
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )