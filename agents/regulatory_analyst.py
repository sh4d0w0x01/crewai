# agents/regulatory_analyst.py
from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

regulatory_analyst = Agent(
    role="Regulatory Analyst",
    goal="Identify regulatory exposures and ongoing investigations or fines relevant to the company.",
    backstory=(
        "A regulatory analyst who finds SEC filings, GDPR investigations, EU AI Act exposures, and other legal/regulatory actions."
    ),
    tools=[search_tool],
    reasoning=(
        "Steps:\n"
        "1. Search for enforcement actions, fines, or investigations.\n"
        "2. Determine regulatory regimes applicable (GDPR, SEC, PCI, SOX, EU AI Act).\n"
        "3. Summarize exposures and potential impacts."
    ),
    memory=True,
    verbose=True,
)
