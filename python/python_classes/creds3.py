import json

from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class Cred3:
    """Credit transaction"""

    def __init__(self, absolute_amount: float, txn_type: str):
        """
        absolute_amount: amount of transaction, always positive
        txn_type: type of transaction
        """
        self.absolute_amount = absolute_amount
        if txn_type == "DEBIT":
            self.amount = absolute_amount * -1
        else:
            self.amount = absolute_amount
        self.txn_type = txn_type

    def save_as_json(self, path: str):
        """path: the path of the file to save the credit to as json"""
        with open(path, "w") as f:
            json.dump({"amount": self.amount, "txn_type": self.txn_type}, f)


credits = [Cred3(r[1], r[2]) for r in rows]
credit = credits[0]

# Next up: use classmethods to make an alternate constructor
