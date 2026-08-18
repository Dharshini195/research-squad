from crew import crew
from dotenv import load_dotenv

load_dotenv()

result = crew.kickoff(
    inputs={
        "topic" : "Latest developments in agentic AI architectures"
    }
)

print(result)