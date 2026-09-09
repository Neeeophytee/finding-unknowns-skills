import unittest

from evals.reproduce import observations


class ExampleReceipts(unittest.TestCase):
    def test_documented_fixture_failures_remain_reproducible(self):
        # A teaching fixture accidentally fixed or changed would invalidate the published example.
        self.assertEqual(observations(), (2, True))
