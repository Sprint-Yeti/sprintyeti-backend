# services/ai_service.py
import os
import time
from functools import wraps
import openai
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

# Configure OpenAI key and LangChain LLM
openai.api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI(model_name="gpt-4", api_key=openAI.api_key, temperature=0.7)


class AIService:
    def __init__(self, max_retries=3, backoff_factor=2):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        # Define prompt templates
        self.task_breakdown_template = PromptTemplate(
            input_variables=["project_desc"],
            template=(
                "You are SprintYeti AI Assistant specialized in project management. "
                "Given the project description below, identify and output a JSON array of tasks. "
                "Each task must include: id, title, description, deadline (ISO 8601 or null), importance (critical, important_not_urgent, urgent_not_important, non_urgent_non_important), "
                "and dependencies (list of ids). "
                "Ensure tasks cover all critical phases and are absolutely required. "
                "Project Description:\n{project_desc}"
            )
        )
        self.command_parse_template = PromptTemplate(
            input_variables=["cmd_text"],
            template=(
                "You are SprintYeti AI Assistant. "
                "Parse the following user command into a strict JSON object with keys: title, description, deadline (ISO 8601 or null), tech_stack (list of strings), phase_focus. "
                "Only output valid JSON.\nCommand:\n{cmd_text}"
            )
        )
        # Create LLM chains
        self.breakdown_chain = LLMChain(
            llm=llm, prompt=self.task_breakdown_template)
        self.parse_chain = LLMChain(
            llm=llm, prompt=self.command_parse_template)

    def _retry(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            retries = 0
            while True:
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries > self.max_retries:
                        raise
                    sleep_time = self.backoff_factor ** retries
                    time.sleep(sleep_time)
        return wrapper

    @_retry
    def task_breakdown(self, project_description: str) -> list:
        """
        Break down a project description into a list of task dicts.
        """
        result = self.breakdown_chain.run(project_desc=project_description)
        # Parse JSON string into Python list
        import json
        tasks = json.loads(result)
        return tasks

    @_retry
    def parse_command(self, command_text: str) -> dict:
        """
        Parse user DSL command into structured JSON fields.
        """
        result = self.parse_chain.run(cmd_text=command_text)
        import json
        cmd_json = json.loads(result)
        return cmd_json
