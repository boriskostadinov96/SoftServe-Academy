import unittest
from src.Task2 import profit


class TestProfitCalculation(unittest.TestCase):

    def test_profit_standard_case(self):
        self.assertEqual(profit({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}), 14796)
        self.assertEqual(profit({"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}), 32411)
        self.assertEqual(profit({"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}), 44030)

    def test_zero_profit(self):
        self.assertEqual(profit({"cost_price": 100.00, "sell_price": 100.00, "inventory": 500}), 0)

    def test_no_inventory(self):
        self.assertEqual(profit({"cost_price": 50.00, "sell_price": 75.00, "inventory": 0}), 0)

    def test_loss_case(self):
        self.assertEqual(profit({"cost_price": 20.00, "sell_price": 15.00, "inventory": 100}), -500)


if __name__ == "__main__":
    unittest.main()
