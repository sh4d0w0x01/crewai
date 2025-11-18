# utils/evaluated_task.py
from crewai import Task
import time

class EvaluatedTask(Task):
    """
    Compatibility wrapper: behaves exactly like a normal Task.
    Kept so existing imports that reference EvaluatedTask don't break.
    """
    def __init__(self, *args, evaluation_mode=None, evaluation_context=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.evaluation_mode = evaluation_mode
        self.evaluation_context = evaluation_context

    def execute(self, context=None):
        start = time.time()
        result = super().execute(context)
        duration = time.time() - start
        # no evaluation, only optional lightweight logging
        try:
            print(f"[EvaluatedTask] {getattr(self.agent,'role', 'agent')} executed in {duration:.2f}s")
        except Exception:
            pass
        return result
