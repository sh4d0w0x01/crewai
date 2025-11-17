# agents/cyber_risk_evaluator.py
from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

cyber_risk_evaluator = Agent(
    role="Cyber Risk Evaluator",
    goal="Assess cybersecurity posture, breach history, vendor/supply chain risk, and CVE exposures.",
    backstory=(
        "A cyber risk specialist who looks for incidents, exposures (CVE), supply-chain weaknesses, "
        "and public security findings for the target organization."
    ),
    tools=[search_tool],
    reasoning=(
        "Steps:\n"
        "1. Search for recent breaches, disclosures, and security advisories.\n"
        "2. Check vendor/supply chain issues and third-party incidents.\n"
        "3. Score each risk (Low/Medium/High) and suggest mitigations."
    ),
    memory=True,
    verbose=True,
)
