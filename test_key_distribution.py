import unittest
from key_distribution import assign_keys

class TestKeyDistribution(unittest.TestCase):
    def test_valid_distribution(self):
        """
        Tests a valid input where all networks can be assigned keys without exceeding any device's key limit.
        """
        networks = [
            ("Alice", "Bob"),
            ("Alice", "Carlos"),
            ("Alice", "David"),
            ("Alice", "Bob", "Carlos", "David"),
        ]
        assignments = assign_keys(networks)
        # We expect 4 unique networks based on the input.
        self.assertEqual(len(assignments), 4)
        
    def test_duplicate_networks(self):
        """
        Tests that duplicate networks are eliminated.
        """
        networks = [
            ("Alice", "Bob"),
            ("Bob", "Alice"),  # Duplicate of the first network.
        ]
        assignments = assign_keys(networks)
        # Even with duplicates, we expect only 1 unique network.
        self.assertEqual(len(assignments), 1)

    def test_key_overflow(self):
        """
        Tests that an error is raised if a person is in more networks than the available key slots (4).
        """
        networks = [
            ("Alice", "Bob"),
            ("Alice", "Carlos"),
            ("Alice", "David"),
            ("Alice", "Eve"),
            ("Alice", "Frank"),  # This fifth network for Alice should trigger an error.
        ]
        with self.assertRaises(Exception) as context:
            assign_keys(networks)
        self.assertIn("Alice's device is out of keys", str(context.exception))

if __name__ == '__main__':
    unittest.main()