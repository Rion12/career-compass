from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from career_compass.sub_agents.advisor import prompt
from career_compass.tools.adk_tools import check_geopolitics_tool

MODEL_NAME = "gemini-2.5-flash-lite"
model = Gemini(model=MODEL_NAME)

advisor_agent = Agent(
    name="Career_Advisor",
    model=model,
    instruction=prompt.ADVISOR_INSTR,
    tools=[check_geopolitics_tool]
)
