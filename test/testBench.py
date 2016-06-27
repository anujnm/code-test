from benchApp import BenchApp
import unittest
from datetime import datetime


class TestBenchApp(unittest.TestCase):
    def setUp(self):
        self.bench_app = BenchApp()
        return

    def test_get_total(self):
        self.assertEqual(self.bench_app.get_total_balance(), 20262.81)

    def test_get_daily_balances(self):
        daily_balances = self.bench_app.get_all_daily_balances()
        self.assertEqual(len(daily_balances), 10)

    def test_get_balance(self):
        current_balance = self.bench_app.get_balance(datetime.now())
        self.assertEqual(round(current_balance, 2), 20262.81)

    def test_get_all_transactions(self):
        all_transactions = self.bench_app.get_all_transactions()
        self.assertEqual(len(all_transactions), 36)

    def test_get_all_insurance_transactions(self):
        insurance_transactions = \
            self.bench_app.get_all_transactions('Insurance Expense')
        self.assertEqual(len(insurance_transactions), 3)