from crewai import Task
from agents.market_analyst import market_analyst

task_market = Task(
    description=(
        "Analyze market trends and sector performance.\n"
        "Steps:\n"
        "1. Identify macroeconomic factors affecting the industry.\n"
        "2. Review demand, sentiment, and growth projections.\n"
        "3. Compare competitors and their recent changes.\n"
        "4. Check news coverage & analyst opinions.\n"
        "5. Provide a short market direction summary."
    ),
    expected_output=(
        "A concise market insight report: current trend, sector status, "
        "sentiment, competitors, and direction outlook."
    ),
    agent=market_analyst,
)
