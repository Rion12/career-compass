from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from career_compass.sub_agents.application import prompt
from career_compass.tools.adk_tools import validate_sop_tool, track_application_tool

MODEL_NAME = "gemini-2.5-flash-lite"
model = Gemini(model=MODEL_NAME)

application_agent = Agent(
    name="Application_Manager",
    model=model,
    instruction=prompt.APPLICATION_INSTR,
    tools=[validate_sop_tool, track_application_tool]
)
