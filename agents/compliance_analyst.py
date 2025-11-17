# agents/compliance_analyst.py
from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

compliance_analyst = Agent(
    role="Compliance Analyst",
    goal="Map company to relevant control frameworks and identify compliance gaps.",
    backstory=(
        "A compliance specialist that maps business services to control frameworks "
        "like ISO 27001 and NIST CSF and finds public evidence of compliance gaps."
    ),
    tools=[search_tool],
    reasoning=(
        "Steps:\n"
        "1. Determine relevant regulations and frameworks (GDPR, SOX, ISO27001, NIST CSF).\n"
        "2. Search public filings/news for evidence of controls (policies, audits, certifications).\n"
        "3. Identify gaps and produce prioritized findings and control mapping."
    ),
    memory=True,
    verbose=True,
)
