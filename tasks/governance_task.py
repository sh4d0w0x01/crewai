# tasks/governance_task.py
from crewai import Task
from agents.strategy_recommender import strategy_recommender  # reuse strategist for combining
# Optionally create a separate governance strategist; reusing strategy_recommender keeps code minimal.

task_governance = Task(
    description=(
        "Combine compliance, security risk, and regulatory reports into a single GRC assessment and prioritized remediation roadmap."
    ),
    expected_output=(
        "A governance and risk report summarizing compliance gaps, cyber risks, regulatory exposures, prioritized recommendations, "
        "and an overall GRC rating."
    ),
    agent=strategy_recommender  # could be a separate agent like 'governance_strategist'
)
