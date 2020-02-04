from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class Cred5:
    """Credit transaction with a property"""

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

    @property
    def is_debit(self) -> bool:
        return self.txn_type == "DEBIT"


credits = [Cred5.from_row(r) for r in rows]
credit = credits[0]
debits_only = [c for c in credits if c.is_debit]
