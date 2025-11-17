from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

strategy_recommender = Agent(
    role="Chief Investment Strategist",
    goal="Combine all analyses to recommend a Buy/Sell/Hold decision.",
    backstory=(
        "A strategic investor who integrates company performance, market dynamics, "
        "and risk assessment into a single actionable recommendation."
    ),
    tools=[search_tool],
    reasoning=(
        "Steps:\n"
        "1. Review all reports.\n"
        "2. Weigh risks vs. growth potential.\n"
        "3. Produce a clear recommendation with reasoning.\n"
        "4. Include two disclaimers."
    ),
    memory=True,
    verbose=True,
)
