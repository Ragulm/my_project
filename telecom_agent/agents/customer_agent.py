from google.adk.agents.llm_agent import Agent
from telecom_agent.tools.customer_tools import validate_customer
from telecom_agent.shared.config import MODEL

customer_agent = Agent(
    name="customer_agent",
    model=MODEL,
    tools=[validate_customer],
)