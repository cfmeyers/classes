from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class Cred2:
    """
    Credit transaction
    """

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


credits = [Cred2(r[1], r[2]) for r in rows]
total = 0.0
for credit in credits:
    total += credit.amount
print(total)

# next up: expand functionality by making another method
