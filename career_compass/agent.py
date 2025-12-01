from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
from career_compass import prompt
from career_compass.sub_agents.advisor.agent import advisor_agent
from career_compass.sub_agents.researcher.agent import researcher_agent
from career_compass.sub_agents.finance.agent import finance_agent
from career_compass.sub_agents.application.agent import application_agent

MODEL_NAME = "gemini-2.5-flash-lite"
model = Gemini(model=MODEL_NAME)

root_agent = Agent(
    name="Career_Compass",
    model=model,
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        advisor_agent,
        researcher_agent,
        finance_agent,
        application_agent
    ]
)
