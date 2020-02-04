from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class Cred1:
    """Credit transaction"""

    def __init__(self, amount, txn_type):
        self.amount = amount
        self.txn_type = txn_type


credits = [Cred1(r[1], r[2]) for r in rows]

total = 0.0
for credit in credits:
    if credit.txn_type == "CREDIT":
        total += credit.amount
    else:
        total -= credit.amount
print(total)
# still requires a fair bit of knowledge about credits (see that conditional)
