from crewai import Task
from agents.regulatory_analyst import regulatory_analyst

task_regulation = Task(
    description=(
        "Assess regulatory exposure.\n"
        "Steps:\n"
        "1. Look for any ongoing legal actions.\n"
        "2. Check compliance with GDPR, SEC, FTC, SOX.\n"
        "3. Identify fines or warnings.\n"
        "4. List compliance obligations by region.\n"
        "5. Provide risk severity."
    ),
    expected_output=(
        "Regulatory risk summary including incidents, obligations, "
        "and potential impact."
    ),
    agent=regulatory_analyst,
)
