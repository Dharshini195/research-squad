from crewai import Agent
from crewai_tools import SerperDevTool
import config

llm=config.llm

search_tool = SerperDevTool()


web_researcher = Agent(
    role="Web Research Specialist",

    goal=(
        "Find relevant and up-to-date information from the web "
        "about the research topic."
    ),

    backstory=(
        "You are an expert research analyst who specializes in "
        "finding reliable information from online sources. "
        "You distinguish useful evidence from low-quality information."
    ),

    tools=[search_tool],
    llm=llm,
    verbose=True
)