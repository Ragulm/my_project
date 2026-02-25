from telecom_agent.shared.state import state

def provision_service() -> dict:

    state.service_active = True

    return {"status": "success", "message": "Service activated"}