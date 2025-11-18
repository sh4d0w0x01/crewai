from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

risk_evaluator = Agent(
    role="Senior Risk Evaluator",
    goal="Identify operational, regulatory, and market risks.",
    backstory=(
        "A strategist experienced in global regulatory environments, "
        "supply chain issues, and business continuity risks."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
