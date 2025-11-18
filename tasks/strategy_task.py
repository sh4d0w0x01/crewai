from crewai import Task
from agents.strategy_recommender import strategy_recommender

task_strategy = Task(
    description=(
        "Provide a final investment recommendation.\n"
        "Steps:\n"
        "1. Review financial, market, and risk outputs.\n"
        "2. Decide whether signals indicate growth or risk.\n"
        "3. Compare opportunities vs challenges.\n"
        "4. Give a Buy / Sell / Hold recommendation.\n"
        "5. Add 2 disclaimer sentences on investment risk."
    ),
    expected_output=(
        "A Buy/Sell/Hold decision with reasoning and 2 disclaimers."
    ),
    agent=strategy_recommender,
)
