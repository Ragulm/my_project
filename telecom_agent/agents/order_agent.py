from google.adk.agents.llm_agent import Agent

from telecom_agent.tools.order_tools import (
    create_order,
    schedule_installation
)

from telecom_agent.shared.config import MODEL

order_agent = Agent(
    name="order_agent",
    model=MODEL,
    tools=[
        create_order,
        schedule_installation
    ],
)