from telecom_agent.shared.state import state

def validate_customer(mobile_number: str) -> dict:

    if len(mobile_number) == 10 and mobile_number.isdigit():

        state.mobile = mobile_number
        state.customer_id = "CUST-" + mobile_number[-4:]

        return {
            "status": "success",
            "customer_id": state.customer_id
        }

    return {"status": "failed", "message": "Invalid mobile number"}