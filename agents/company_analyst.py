from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

company_analyst = Agent(
    role="Senior Company Analyst",
    goal="Analyze company financial health and key performance metrics.",
    backstory=(
        "A data-driven analyst skilled in interpreting earnings reports, "
        "cash flow statements, and revenue growth patterns."
    ),
    tools=[search_tool],
    reasoning=(
        "Think step-by-step:\n"
        "1. Identify key financial metrics.\n"
        "2. Compare with last 2 quarters.\n"
        "3. Evaluate profit margins, cash flow, and growth.\n"
        "4. Summarize with numeric insights and confidence score."
    ),
    memory=True,
    verbose=True,
)
