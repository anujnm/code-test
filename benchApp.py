from transaction import Transaction

from sets import Set
from datetime import datetime
import requests
import sys


BASE_URL = 'http://resttest.bench.co/transactions/'
URL_SUFFIX = '.json'
KEYWORDS = Set(["AB", "BC", "DHL", "YVR"])


class BenchApp(object):

    def __init__(self):
        """
        Initialises app- makes request to API for data, processes and stores it
        """
        self.all_transactions = set()
        self.total = 0
        self.category_data = {}
        self.category_totals = {}
        self.daily_balances = {}
        self.__request_data()
        self.__process_data()

    def __process_data(self):
        """
        Process transaction data so that its available in multiple formats
        """
        # Sum of transactions for each day
        # daily_transactions = {date: total transactional amount for that day}
        daily_transactions = {}

        for transaction in self.all_transactions:
            self.total += transaction.amount
            if transaction.ledger in self.category_data:
                self.category_data[transaction.ledger].append(transaction)
                self.category_totals[transaction.ledger] += transaction.amount
            else:
                self.category_data[transaction.ledger] = [transaction]
                self.category_totals[transaction.ledger] = transaction.amount

            if transaction.date in daily_transactions:
                daily_transactions[transaction.date] += transaction.amount
            else:
                daily_transactions[transaction.date] = transaction.amount

        # Use daily_transactions to create a hashmap of cumulative transactions
        sorted_dates = sorted(daily_transactions)
        for index, date in enumerate(sorted_dates):
            if index == 0:
                self.daily_balances[date] = daily_transactions[date]
            else:
                self.daily_balances[date] = \
                    self.daily_balances[sorted_dates[index - 1]] + \
                    daily_transactions[date]

    def __request_data(self):
        """
        Get transaction data from the API and populate self.all_transactions
        """

        index = 1  # the API doesn't return anything for index 0
        number_transactions = 0
        total_transactions = float("inf")  # update the value once it is known
        while number_transactions < total_transactions:
            url = BASE_URL + str(index) + URL_SUFFIX
            try:
                req = requests.get(url)
                data = req.json()
            except ValueError:
                # If the API 404's, break out of the loop and return
                break
            if total_transactions == float("inf"):
                total_transactions = data['totalCount']

            for transaction_data in data['transactions']:
                company_str = str(transaction_data['Company'])
                company = " ".join(
                    word if word in KEYWORDS else word.capitalize()
                    for word in company_str.split())

                transaction = Transaction(
                    amount=float(transaction_data['Amount']),
                    company=company,
                    date=datetime.strptime(transaction_data['Date'],
                                           '%Y-%m-%d'),
                    ledger=str(transaction_data['Ledger']),
                )
                self.all_transactions.add(transaction)
                number_transactions += 1
            index += 1

    def get_total_balance(self, category=None):
        """
        Get total balance for inputted category. If no category is inputted,
        total balance for all transactions is returned

        Args:
            category -- category to get balance for

        Returns:
            float: The total balance for inputted category

        Raises:
            AttributeError: When the given category cannot be found
        """
        if not category:
            return self.total
        elif category not in self.category_totals:
            raise AttributeError("Could not find category " + str(category))
        else:
            return self.category_totals[category]

    def get_all_daily_balances(self):
        """
        Get daily balance for each unique day

        Returns:
            Dictionaries with date: total for all dates in transactions
        """
        return self.daily_balances

    def get_balance(self, date=datetime.now()):
        """
        Get daily balance for given date (EOD balance)

        Returns
            float: daily balance for that day. 0 if date is prior to all
            transactions.
        """
        max_previous_date = max(dt for dt in self.daily_balances if dt <= date)
        if max_previous_date:
            return self.daily_balances[max_previous_date]
        return float(0)

    def get_all_transactions(self, category=None):
        """
        Get all transactions for inputted category. If no category is inputted,
        all transactions for all categories are returned

        Args:
            category -- category to get transactions for

        Returns:
            list: List of transactions

        Raises:
            AttributeError: When the given category cannot be found
        """
        if not category:
            return self.all_transactions
        elif category not in self.category_data:
            raise AttributeError("Could not find category " + str(category))
        else:
            return self.category_data[category]

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise AttributeError("Please indicate what data you want")

    bench_app = BenchApp()

    if sys.argv[1] == 'transactions':
        if len(sys.argv) == 2:
            print bench_app.get_all_transactions()
        else:
            print bench_app.get_all_transactions(sys.argv[2])
    elif sys.argv[1] == 'total':
        if len(sys.argv) == 2:
            print bench_app.get_total_balance()
        else:
            print bench_app.get_total_balance(sys.argv[2])
    elif sys.argv[1] == 'balance':
        if len(sys.argv) == 2:
            print bench_app.get_balance()
        elif sys.argv == 'all':
            print bench_app.get_all_daily_balances()
        else:
            date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
            print bench_app.get_balance(date)
    else:
        raise AttributeError("Please read the docs to see available functions")
