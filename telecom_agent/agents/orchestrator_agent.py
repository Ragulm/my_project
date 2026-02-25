from google.adk.agents.llm_agent import Agent

from telecom_agent.agents.customer_agent import customer_agent
from telecom_agent.agents.qualification_agent import qualification_agent
from telecom_agent.agents.order_agent import order_agent
from telecom_agent.agents.provisioning_agent import provisioning_agent
from telecom_agent.agents.support_agent import support_agent

from telecom_agent.shared.config import MODEL


orchestrator_agent = Agent(

    name="telecom_orchestrator",

    model=MODEL,

    description="Telecom Fiber Order Journey Orchestrator",

    instruction="""
You are a telecom fiber order assistant.

Guide the user step-by-step through telecom order workflow.

Workflow steps:

1 Ask mobile number → use customer_agent

2 Ask address → use qualification_agent

3 Check service availability → use qualification_agent

4 Ask budget → recommend plan → use qualification_agent

5 Create order → use order_agent

6 Schedule installation → use order_agent

7 Activate service → use provisioning_agent

8 Provide order status → use support_agent

Rules:

• Do NOT execute everything automatically  
• Ask user step-by-step  
• Use correct sub_agent based on user input  
• Always use tools when required  
• Maintain conversational telecom workflow  

Goal: Successfully activate telecom fiber connection.
""",

    sub_agents=[
        customer_agent,
        qualification_agent,
        order_agent,
        provisioning_agent,
        support_agent
    ]

)