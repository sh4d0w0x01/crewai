from crewai import Task
from agents.company_analyst import company_analyst

task_company = Task(
    description=(
        "Analyze company financial performance.\n"
        "Steps:\n"
        "1. Retrieve the latest financial reports.\n"
        "2. Identify revenue, profit margin, cash flow, debt, and expenses.\n"
        "3. Compare data with previous 2 quarters.\n"
        "4. Highlight trends or anomalies.\n"
        "5. Provide numeric insights with summary."
    ),
    expected_output=(
        "A structured financial analysis report including metrics, "
        "trends, and key insights supported with data."
    ),
    agent=company_analyst,
)
