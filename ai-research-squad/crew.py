from crewai import Crew, Process

from agents.web_researcher import web_researcher
from agents.technical_analyst import technical_analyst
from agents.industry_analyst import industry_analyst
from agents.report_writer import report_writer

from tasks.web_research_task import web_research_task
from tasks.technical_analyst_task import technical_analysis_task
from tasks.industry_analyst_task import industry_analysis_task
from tasks.report_writing_task import report_writing_task

crew = Crew(
    agents=[
        web_researcher,
        technical_analyst,
        industry_analyst,
        report_writer
    ],

    tasks=[
        web_research_task,
        technical_analysis_task,
        industry_analysis_task,
        report_writing_task
    ],

    process=Process.sequential,

    verbose=True
)