from crewai.flow.flow import Flow, start, listen
from crew import crew
from dotenv import load_dotenv

load_dotenv()
class ResearchFlow(Flow):

    @start()
    def run_research(self):

        topic = "How AI coding agents are changing software development in 2026"

        print(f"\nResearch topic: {topic}\n")

        result = crew.kickoff(
            inputs={
                "topic": topic
            }
        )

        return result


if __name__ == "__main__":

    flow = ResearchFlow()

    result = flow.kickoff()

    print("\n==============================")
    print("FINAL RESEARCH REPORT")
    print("==============================\n")

    print(result)