from google.adk.agents.llm_agent import Agent

from telecom_agent.tools.support_tools import check_order_status
from telecom_agent.shared.config import MODEL

support_agent = Agent(
    name="support_agent",
    model=MODEL,
    tools=[check_order_status],
)