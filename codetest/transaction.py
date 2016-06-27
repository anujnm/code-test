class Transaction(object):

    def __init__(self, amount, company, date, ledger):
        self.amount = amount
        self.company = company
        self.date = date
        self.ledger = ledger

    def __unicode__(self):
        """
        Returns a String representation of the object
        Equivalent to Java's toString() method
        """
        return \
            '\nAmount: {}, Company: {}, Date: {}, Ledger: {}'.format(
                self.amount, self.company, self.date, self.ledger)

    def __str__(self):
        """
        Old method for returning a String representation of the object
        """
        return unicode(self).encode('utf-8')

    def __eq__(self, other):
        """
        Overriding the equals operator
        Checks each data field is the same for both objects while ignoring case
        """
        return \
            self.amount == other.amount and \
            self.company.lower() == other.company.lower() and \
            self.date == other.date and \
            self.ledger.lower() == other.ledger.lower()

    def __hash__(self):
        """
        Overriding the hash function to allow objects in sets/lists to be
        compared
        """
        return hash(self.__repr__())

    def __repr__(self):
        """
        Overriding this function to
        """
        return unicode(self)

