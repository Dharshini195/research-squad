from crewai import Task

from agents.web_researcher import web_researcher


web_research_task = Task(
    description=(
        "Research the following topic: {topic}.\n\n"
        "Use the web search tool to find reliable and recent "
        "information relevant to the topic.\n\n"
        "Focus on factual information, important developments, "
        "and useful evidence."
    ),

    expected_output=(
        "A structured collection of research findings with "
        "important facts and source information."
    ),

    agent=web_researcher
)