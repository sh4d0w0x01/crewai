from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

controller_agent = Agent(
    role="Controller Agent",
    goal="Collect company metadata and initialize crew context.",
    backstory=(
        "Responsible for gathering essential company data (ticker, sector, summary) "
        "before deeper analysis begins."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
