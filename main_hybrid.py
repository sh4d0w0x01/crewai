# main_hybrid.py
import os

try:
    from google.colab import userdata
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY") or userdata.get('OPENAI_API_KEY')
    os.environ["SERPER_API_KEY"] = os.environ.get("SERPER_API_KEY") or userdata.get('SERPER_API_KEY')
    os.environ["FI_API_KEY"] = os.environ.get("FI_API_KEY") or userdata.get('FI_API_KEY')
    os.environ["FI_SECRET_KEY"] = os.environ.get("FI_SECRET_KEY") or userdata.get('FI_SECRET_KEY')
except Exception:
    pass

missing = [k for k in ("OPENAI_API_KEY", "FI_API_KEY", "FI_SECRET_KEY") if not os.environ.get(k)]
if missing:
    print(f"Warning: Missing environment variables: {missing} (tracing or OpenAI may not work)")

# initialize tracing (side-effect: instruments CrewAI)
from utils import evaluation_utils  # keeps variable name from before; this file now only init tracing

from crewai import Crew, Process

# Use the plain tasks (no evaluated tasks)
from tasks.company_task import task_company
from tasks.market_task import task_market
from tasks.risk_task import task_risk
from tasks.strategy_task import task_strategy

from tasks.compliance_task import task_compliance
from tasks.security_risk_task import task_security_risk
from tasks.regulation_task import task_regulation
from tasks.governance_task import task_governance

# optional controller (keeps metadata logic)
from agents.controller_agent import controller_agent

investment_crew = Crew(
    agents=[],
    tasks=[
        task_market,
        task_company,
        task_risk,
        task_strategy
    ],
    process=Process.sequential,
    verbose=True
)

grc_crew = Crew(
    agents=[],
    tasks=[
        task_compliance,
        task_security_risk,
        task_regulation,
        task_governance
    ],
    process=Process.sequential,
    verbose=True
)

def run_all(topic: str = "NVIDIA"):
    print("\n🚀 Running Investment pipeline...")
    inv_results = investment_crew.kickoff()
    print("\n--- Investment Results ---")
    print(inv_results)

    print("\n🚀 Running GRC pipeline...")
    grc_results = grc_crew.kickoff()
    print("\n--- GRC Results ---")
    print(grc_results)

    return inv_results, grc_results

if __name__ == "__main__":
    run_all("NVIDIA")
