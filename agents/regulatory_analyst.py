from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

regulatory_analyst = Agent(
    role="Regulatory Analyst",
    goal="Find legal risks, ongoing investigations, fines, and obligations.",
    backstory=(
        "An analyst with expertise in EU, US, and international regulations, "
        "including GDPR, SEC, SOX, CCPA, and AI governance laws."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
