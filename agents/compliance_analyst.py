from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

compliance_analyst = Agent(
    role="Compliance Analyst",
    goal="Map company controls to ISO 27001, SOC2, NIST-CSF, GDPR, etc.",
    backstory=(
        "An analyst experienced in compliance frameworks and public "
        "evidence collection for certification readiness."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
