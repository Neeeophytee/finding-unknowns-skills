import unittest

from permissions import can_read
from webhooks import accept_event


class Baseline(unittest.TestCase):
    def test_event_is_accepted(self):
        orders = []
        self.assertEqual(accept_event(orders, {"id": "evt-1", "item": "book"}), {"status": "accepted"})
        self.assertEqual(len(orders), 1)

    def test_owner_can_read(self):
        self.assertTrue(can_read({"id": "u1", "role": "member", "tenant": "a"}, {"owner_id": "u1", "tenant": "a"}))

    def test_other_member_cannot_read(self):
        self.assertFalse(can_read({"id": "u2", "role": "member", "tenant": "a"}, {"owner_id": "u1", "tenant": "a"}))

    def test_admin_can_read_within_tenant(self):
        self.assertTrue(can_read({"id": "u2", "role": "admin", "tenant": "a"}, {"owner_id": "u1", "tenant": "a"}))


if __name__ == "__main__":
    unittest.main()
