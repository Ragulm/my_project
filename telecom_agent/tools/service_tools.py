from telecom_agent.shared.state import state

def validate_address(address: str) -> dict:

    state.address = address

    return {"status": "success", "message": "Address validated"}


def check_service_availability(pincode: str) -> dict:

    if pincode.startswith("6"):

        return {
            "status": "success",
            "available": True,
            "plans": ["Fiber 100 Mbps", "Fiber 200 Mbps"]
        }

    return {"status": "failed", "available": False}


def recommend_plan(budget: int) -> dict:

    if budget <= 500:
        plan = "Fiber 100 Mbps"
    else:
        plan = "Fiber 200 Mbps"

    state.plan = plan

    return {"status": "success", "plan": plan}