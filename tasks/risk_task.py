from crewai import Task
from agents.risk_evaluator import risk_evaluator

task_risk = Task(
    description=(
        "Identify business risks.\n"
        "Steps:\n"
        "1. Investigate geopolitical, market, and supply-chain risks.\n"
        "2. Find competitive threats.\n"
        "3. Review regulatory filings for risk disclosures.\n"
        "4. Categorize risks as Low, Medium, or High.\n"
        "5. Provide mitigation suggestions."
    ),
    expected_output=(
        "A business risk report containing risk types, severity level "
        "and recommended mitigation strategies."
    ),
    agent=risk_evaluator,
)
