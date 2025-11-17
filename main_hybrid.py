# main_hybrid.py
import os
try:
    # google colab userdata if running in Colab
    from google.colab import userdata
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY") or userdata.get('OPENAI_API_KEY')
    os.environ["FI_API_KEY"] = os.environ.get("FI_API_KEY") or userdata.get('FI_API_KEY')
    os.environ["FI_SECRET_KEY"] = os.environ.get("FI_SECRET_KEY") or userdata.get('FI_SECRET_KEY')
    os.environ["SERPER_API_KEY"] = os.environ.get("SERPER_API_KEY") or userdata.get('SERPER_API_KEY')
except Exception:
    # not in Colab; expect env vars already set
    pass

from fi_instrumentation import register
from fi_instrumentation.fi_types import ProjectType
from traceai_crewai import CrewAIInstrumentor

# Instrumentation
trace_provider = register(
    project_type=ProjectType.OBSERVE,
    project_name="crewai_hybrid_project"
)
CrewAIInstrumentor().instrument(tracer_provider=trace_provider)

# Import agents and tasks (investment)
from agents.market_analyst import market_analyst
from agents.company_analyst import company_analyst
from agents.risk_evaluator import risk_evaluator  # business risk
from agents.strategy_recommender import strategy_recommender
from agents.controller_agent import controller_agent

from tasks.market_task import task_market
from tasks.company_task import task_company
from tasks.risk_task import task_risk
from tasks.strategy_task import task_strategy

# Import GRC agents & tasks
from agents.compliance_analyst import compliance_analyst
from agents.cyber_risk_evaluator import cyber_risk_evaluator
from agents.regulatory_analyst import regulatory_analyst

from tasks.compliance_task import task_compliance
from tasks.security_risk_task import task_security_risk
from tasks.regulation_task import task_regulation
from tasks.governance_task import task_governance

from crewai import Crew, Process

# Investment crew (existing pipeline)
investment_crew = Crew(
    agents=[
        market_analyst,
        company_analyst,
        risk_evaluator,
        strategy_recommender,
    ],
    tasks=[
        task_market,
        task_company,
        task_risk,
        task_strategy,
    ],
    process=Process.sequential,
    verbose=True
)

# GRC crew (new pipeline)
grc_crew = Crew(
    agents=[
        controller_agent,       # controller can prepare exec context for GRC as well
        compliance_analyst,
        cyber_risk_evaluator,
        regulatory_analyst,
        strategy_recommender,   # reused for synthesis (or create a separate governance strategist)
    ],
    tasks=[
        task_compliance,
        task_security_risk,
        task_regulation,
        task_governance,
    ],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Running Investment pipeline...")
    investment_results = investment_crew.kickoff()
    print("\n--- Investment Results ---")
    print(investment_results)

    print("\n🚀 Running GRC (Governance, Risk & Compliance) pipeline...")
    grc_results = grc_crew.kickoff()
    print("\n--- GRC Results ---")
    print(grc_results)
