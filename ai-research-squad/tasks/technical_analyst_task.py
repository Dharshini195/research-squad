from crewai import Task

from agents.technical_analyst import technical_analyst
from tasks.web_research_task import web_research_task


technical_analysis_task = Task(
    description=(
        "Analyze the technical aspects of: {topic}.\n\n"
        "Use the findings from the previous research task "
        "as evidence for your analysis.\n\n"
        "Focus on architecture, performance, scalability, "
        "latency, cost, implementation complexity, and "
        "engineering trade-offs."
    ),

    expected_output=(
        "A detailed technical analysis explaining the major "
        "engineering considerations and trade-offs."
    ),

    context=[web_research_task],

    agent=technical_analyst
)