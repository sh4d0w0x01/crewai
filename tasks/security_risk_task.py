# tasks/security_risk_task.py
from crewai import Task
from agents.cyber_risk_evaluator import cyber_risk_evaluator

task_security_risk = Task(
    description=(
        "Analyze cybersecurity posture: breaches, CVEs, third-party incidents, and supply chain threats."
    ),
    expected_output=(
        "A scored list of cybersecurity risks (Low/Medium/High) with supporting evidence and mitigation recommendations."
    ),
    agent=cyber_risk_evaluator,
    context=[]
)
