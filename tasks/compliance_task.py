from crewai import Task
from agents.compliance_analyst import compliance_analyst

task_compliance = Task(
    description=(
        "Analyze compliance posture.\n"
        "Steps:\n"
        "1. Check relevance with ISO27001, NIST-CSF, GDPR, SOC2.\n"
        "2. Search for public compliance indicators.\n"
        "3. Identify potential gaps in process or documentation.\n"
        "4. Map controls where possible.\n"
        "5. Summarize findings."
    ),
    expected_output=(
        "A short compliance report with control mapping and gap detection."
    ),
    agent=compliance_analyst,
)
