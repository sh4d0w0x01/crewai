# agents/controller_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool

# (Optional) Give it a search tool if you want it to fetch data too
search_tool = SerperDevTool()

controller_agent = Agent(
    role="Controller Agent",
    goal="Collect company metadata and initialize analysis context for the crew.",
    backstory=(
        "You are responsible for orchestrating the overall workflow. "
        "You gather metadata such as ticker symbol, sector, and a brief business summary, "
        "then distribute that to all other agents before analysis begins."
    ),
    reasoning=(
        "Step-by-step approach:\n"
        "1. Identify the company name provided by the user.\n"
        "2. Search for key details: ticker, sector, market cap, summary.\n"
        "3. Build a context dictionary.\n"
        "4. Share it with all agents before execution."
    ),
    tools=[search_tool],
    memory=True,
    verbose=True,
)
