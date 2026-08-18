from crewai import Agent
import config

llm=config.llm

technical_analyst = Agent(
    role="Technical AI Analyst",

    goal=(
        "Analyze the technical aspects of the research topic, "
        "including architecture, performance, scalability, "
        "limitations, and engineering trade-offs."
    ),

    backstory=(
        "You are a senior AI systems engineer with deep knowledge "
        "of LLMs, RAG, vector databases, inference systems, "
        "and enterprise AI architectures."
    ),
    llm=llm,
    verbose=True
)