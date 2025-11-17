from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

risk_evaluator = Agent(
    role="Senior Risk Evaluator",
    goal="Identify operational, regulatory, and market risks for the target company.",
    backstory="A risk strategist with expertise in global regulations, market volatility, and business continuity.",
    tools=[search_tool],
    reasoning=(
        "Steps:\n"
        "1. Search for recent risk factors.\n"
        "2. Identify geopolitical and supply chain threats.\n"
        "3. Score risk severity (Low/Medium/High).\n"
        "4. Suggest mitigations."
    ),
    memory=True,
    verbose=True,
)
