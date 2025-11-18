# utils/evaluation_utils.py
import os
from fi_instrumentation import register, FITracer
from fi_instrumentation.fi_types import ProjectType
from traceai_crewai import CrewAIInstrumentor

# Initialize FutureAGI tracing / instrumentation
def init_tracing(project_name: str = "crewai_hybrid_project"):
    """
    Initializes FutureAGI tracing and auto-instruments CrewAI.
    Expects FI_API_KEY and FI_SECRET_KEY in env vars.
    """
    trace_provider = register(
        project_type=ProjectType.OBSERVE,
        project_name=project_name,
        set_global_tracer_provider=True
    )

    CrewAIInstrumentor().instrument(tracer_provider=trace_provider)

    tracer = FITracer(trace_provider.get_tracer(__name__))
    return trace_provider, tracer

# Initialize on import (idempotent)
trace_provider, tracer = init_tracing()
