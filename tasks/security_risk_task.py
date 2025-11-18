from crewai import Task
from agents.cyber_risk_evaluator import cyber_risk_evaluator

task_security_risk = Task(
    description=(
        "Identify cybersecurity posture.\n"
        "Steps:\n"
        "1. Check for any recent data breaches or cyber incidents.\n"
        "2. Find CVEs tied to vendors, systems, or product lines.\n"
        "3. Inspect supply-chain security.\n"
        "4. Identify critical third-party risks.\n"
        "5. Suggest mitigation steps."
    ),
    expected_output=(
        "Cyber risk report detailing exposures, CVEs, incidents, "
        "and risk mitigation ideas."
    ),
    agent=cyber_risk_evaluator,
)
