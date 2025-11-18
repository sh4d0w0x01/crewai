from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

strategy_recommender = Agent(
    role="Chief Investment Strategist",
    goal="Provide a Buy/Sell/Hold investment call using all prior outputs.",
    backstory=(
        "A financial strategist known for turning research and risk reports "
        "into actionable investment decisions."
    ),
    tools=[search_tool],
    reasoning=True,
    memory=True,
    verbose=True,
)
