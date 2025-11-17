# tasks/compliance_task.py
from crewai import Task
from agents.compliance_analyst import compliance_analyst

task_compliance = Task(
    description=(
        "Map the target company's operations to relevant control frameworks (ISO 27001, NIST CSF) "
        "and identify potential compliance gaps from public sources."
    ),
    expected_output=(
        "Control mapping, list of likely compliance gaps, and prioritized remediation suggestions."
    ),
    agent=compliance_analyst,
    context=[]
)
