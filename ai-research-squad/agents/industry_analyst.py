from crewai import Agent
from crewai_tools import SerperDevTool
import config

llm = config.llm
search_tool = SerperDevTool()


industry_analyst = Agent(
    role="Enterprise AI Industry Analyst",

    goal=(
        "Analyze how the technology is being used in real-world "
        "enterprise environments and identify business implications."
    ),

    backstory=(
        "You are an enterprise technology analyst who studies "
        "AI adoption, business use cases, costs, risks, and "
        "organizational impact."
    ),

    tools=[search_tool],
    llm=llm,

    verbose=True
)