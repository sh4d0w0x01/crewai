from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

company_analyst = Agent(
    role="Senior Company Analyst",
    goal="Analyze company financial health and key performance metrics.",
    backstory=(
        "A data-driven analyst skilled in interpreting earnings reports, "
        "cash flow statements, and revenue growth patterns."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
