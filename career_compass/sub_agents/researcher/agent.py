from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from career_compass.sub_agents.researcher import prompt
from career_compass.tools.adk_tools import search_universities_tool

MODEL_NAME = "gemini-2.5-flash-lite"
model = Gemini(model=MODEL_NAME)

researcher_agent = Agent(
    name="University_Researcher",
    model=model,
    instruction=prompt.RESEARCHER_INSTR,
    tools=[search_universities_tool]
)
