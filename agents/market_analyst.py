from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

market_analyst = Agent(
    role="Senior Market Analyst",
    goal="Analyze market trends, sector dynamics, and competitor performance.",
    backstory=(
        "A seasoned analyst who identifies macroeconomic trends "
        "and competitive forces affecting company growth."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
