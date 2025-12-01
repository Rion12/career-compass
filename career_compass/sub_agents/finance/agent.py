from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from career_compass.sub_agents.finance import prompt
from career_compass.tools.adk_tools import calculate_budget_tool

MODEL_NAME = "gemini-2.5-flash-lite"
model = Gemini(model=MODEL_NAME)

finance_agent = Agent(
    name="Financial_Planner",
    model=model,
    instruction=prompt.FINANCE_INSTR,
    tools=[calculate_budget_tool]
)
