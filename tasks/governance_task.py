from crewai import Task
from agents.strategy_recommender import strategy_recommender

task_governance = Task(
    description=(
        "Create a full GRC (Governance, Risk, Compliance) overview.\n"
        "Steps:\n"
        "1. Summarize compliance, cyber, and regulatory reports.\n"
        "2. Identify top 3 highest risks.\n"
        "3. Create risk mitigation roadmap.\n"
        "4. Assign priority levels.\n"
        "5. Provide final GRC status score."
    ),
    expected_output=(
        "A structured GRC report with priority roadmap and overall posture rating."
    ),
    agent=strategy_recommender,
)
