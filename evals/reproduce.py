#!/usr/bin/env python3
"""Reproduce documented fixture observations; this does not evaluate an agent."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "fixtures"))
from permissions import can_read
from webhooks import accept_event


def observations():
    orders = []
    event = {"id": "evt-1", "item": "book"}
    accept_event(orders, event)
    accept_event(orders, event)
    access = can_read({"id": "admin-a", "role": "admin", "tenant": "a"}, {"owner_id": "owner-b", "tenant": "b"})
    return len(orders), access


if __name__ == "__main__":
    orders, access = observations()
    print(f"Same event delivered twice: {orders} orders (desired: 1)")
    print(f"Tenant A admin can read tenant B document: {access} (desired: False)")
    print("These are deliberately flawed teaching fixtures, not defects in the shipped skills.")
