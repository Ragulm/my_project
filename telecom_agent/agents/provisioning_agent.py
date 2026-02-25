from google.adk.agents.llm_agent import Agent

from telecom_agent.tools.provisioning_tools import provision_service
from telecom_agent.shared.config import MODEL

provisioning_agent = Agent(
    name="provisioning_agent",
    model=MODEL,
    tools=[provision_service],
)