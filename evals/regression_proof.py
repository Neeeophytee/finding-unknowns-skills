"""Deterministic teaching example, not an agent evaluation. Run from repo root."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evals.fixtures.webhooks import accept_event


def incomplete_fix(orders, event):
    if not orders:
        accept_event(orders, event)


def fixed(orders, event):
    if not any(order["event_id"] == event["id"] for order in orders):
        accept_event(orders, event)


def checks(handler):
    orders = []
    event = {"id": "one", "item": "book"}
    handler(orders, event)
    handler(orders, event)
    duplicate_ok = len(orders) == 1
    handler(orders, {"id": "two", "item": "book"})
    distinct_ok = [o["event_id"] for o in orders] == ["one", "two"]
    return duplicate_ok, distinct_ok


if __name__ == "__main__":
    for name, handler, expected in [
        ("original", accept_event, (False, False)),
        ("incomplete fix", incomplete_fix, (True, False)),
        ("fixed", fixed, (True, True)),
    ]:
        result = checks(handler)
        assert result == expected, (name, result)
        print(f"{name}: duplicate replay={result[0]}, distinct events={result[1]}")
