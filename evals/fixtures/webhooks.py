"""Small local teaching fixture. No network, persistence, or production data."""


def accept_event(orders, event):
    orders.append({"event_id": event["id"], "item": event["item"]})
    return {"status": "accepted"}
