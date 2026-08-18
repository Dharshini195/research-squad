from crewai import Task

from agents.industry_analyst import industry_analyst
from tasks.web_research_task import web_research_task
from tasks.technical_analyst_task import technical_analysis_task


industry_analysis_task = Task(
    description=(
        "Analyze the enterprise and business implications of: {topic}.\n\n"
        "Research real-world applications, adoption patterns, "
        "business benefits, risks, and cost considerations."
    ),

    expected_output=(
        "A structured enterprise analysis covering real-world "
        "applications, benefits, risks, and business trade-offs."
    ),
    context=[web_research_task],

    agent=industry_analyst
)