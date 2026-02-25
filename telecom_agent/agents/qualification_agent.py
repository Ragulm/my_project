from google.adk.agents.llm_agent import Agent

from telecom_agent.tools.service_tools import (
    validate_address,
    check_service_availability,
    recommend_plan
)

from telecom_agent.shared.config import MODEL

qualification_agent = Agent(
    name="qualification_agent",
    model=MODEL,
    tools=[
        validate_address,
        check_service_availability,
        recommend_plan
    ],
)