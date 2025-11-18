from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

cyber_risk_evaluator = Agent(
    role="Cyber Risk Evaluator",
    goal="Look for cyber incidents, CVEs, and supply-chain vulnerabilities.",
    backstory=(
        "A cybersecurity expert skilled in threat intelligence, vendor risk review, "
        "and exposure assessment."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
