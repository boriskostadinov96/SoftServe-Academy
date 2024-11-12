import unittest

from src.Task9 import greeting


class TestGreetingFunction(unittest.TestCase):

    def test_name_in_guest_list(self):
        self.assertEqual(greeting("Randy"), "Hi! I'm Randy, and I'm from Germany.")
        self.assertEqual(greeting("Karla"), "Hi! I'm Karla, and I'm from France.")
        self.assertEqual(greeting("Wendy"), "Hi! I'm Wendy, and I'm from Japan.")
        self.assertEqual(greeting("Norman"), "Hi! I'm Norman, and I'm from England.")
        self.assertEqual(greeting("Sam"), "Hi! I'm Sam, and I'm from Argentina.")

    def test_name_not_in_guest_list(self):
        self.assertEqual(greeting("John"), "Hi! I'm a guest.")
        self.assertEqual(greeting("Alice"), "Hi! I'm a guest.")
        self.assertEqual(greeting("Bob"), "Hi! I'm a guest.")


if __name__ == "__main__":
    unittest.main()
