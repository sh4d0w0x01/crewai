# tasks/regulation_task.py
from crewai import Task
from agents.regulatory_analyst import regulatory_analyst

task_regulation = Task(
    description=(
        "Identify regulatory investigations, fines, and legal exposures applicable to the company (SEC, GDPR, EU AI Act, SOX, etc.)."
    ),
    expected_output=(
        "Regulatory exposure summary, relevant cases/filings, and an assessment of potential financial or operational impact."
    ),
    agent=regulatory_analyst,
    context=[]
)
