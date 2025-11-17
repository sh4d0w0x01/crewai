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
    reasoning=(
        "Process:\n"
        "1. Retrieve current market trends.\n"
        "2. Analyze competitors (AMD, Intel, etc.).\n"
        "3. Assess sentiment from recent news.\n"
        "4. Output concise insights with market direction."
    ),
    memory=True,
    verbose=True,
)
