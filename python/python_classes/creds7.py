from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class UserTable:
    table = ""
    user_join_column = ""

    def debug_sql(self):
        return f"""\
        SELECT
            u.*
            , t.*
        FROM users u
            LEFT OUTER JOIN {self.table} t
                ON u.{self.user_join_column} = t.{self.user_join_column}
        WHERE user_id = {self.user_id}
        """


class Cred7(UserTable):
    """Credit transaction that inherits from UserTable"""

    table = "credits"
    user_join_column = "user_id"

    def __init__(self, user_id: int, absolute_amount: float, txn_type: str):
        """
        absolute_amount: amount of transaction, always positive
        txn_type: type of transaction
        """
        self.absolute_amount = absolute_amount
        self.user_id = user_id
        if txn_type == "DEBIT":
            self.amount = absolute_amount * -1
        else:
            self.amount = absolute_amount
        self.txn_type = txn_type

    @classmethod
    def from_row(cls, row):
        return cls(user_id=row[0], absolute_amount=row[1], txn_type=row[2])


credits = [Cred7.from_row(r) for r in rows]
credit = credits[0]
