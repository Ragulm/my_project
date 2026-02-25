from telecom_agent.shared.state import state

def check_order_status() -> dict:

    return {
        "customer_id": state.customer_id,
        "mobile": state.mobile,
        "address": state.address,
        "plan": state.plan,
        "order_id": state.order_id,
        "service_active": state.service_active
    }