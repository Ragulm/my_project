import uuid
from telecom_agent.shared.state import state

def create_order() -> dict:

    order_id = "ORD-" + str(uuid.uuid4())[:8]

    state.order_id = order_id

    return {"status": "success", "order_id": order_id}


def schedule_installation(date: str) -> dict:

    appointment_id = "APT-" + str(uuid.uuid4())[:8]

    state.appointment_id = appointment_id

    return {"status": "success", "appointment_id": appointment_id}