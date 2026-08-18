from crewai import Task

from agents.report_writer import report_writer

from tasks.web_research_task import web_research_task
from tasks.technical_analyst_task import technical_analysis_task
from tasks.industry_analyst_task import industry_analysis_task


report_writing_task = Task(
    description=(
        "Create a comprehensive research report about: {topic}.\n\n"

        "Use the outputs from the web research, technical analysis, "
        "and industry analysis tasks as your source material.\n\n"

        "The report should contain:\n"
        "1. Executive Summary\n"
        "2. Introduction\n"
        "3. Key Findings\n"
        "4. Technical Analysis\n"
        "5. Enterprise/Business Analysis\n"
        "6. Advantages and Disadvantages\n"
        "7. Recommendations\n"
        "8. Conclusion\n\n"

        "Do not introduce unsupported claims. "
        "Clearly distinguish research findings from your own synthesis."
    ),

    expected_output=(
        "A polished, professional research report with clear sections, "
        "logical reasoning, and conclusions supported by the research."
    ),

    context=[
        web_research_task,
        technical_analysis_task,
        industry_analysis_task
    ],

    agent=report_writer
)