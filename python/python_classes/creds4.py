from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class Cred4:
    """Credit transaction with a helpful constructor"""

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

    @classmethod
    def from_row(cls, row):
        return cls(absolute_amount=row[1], txn_type=row[2])


credits = [Cred4.from_row(r) for r in rows]

# Next up: use @property decorator to add pseudo-properties
