from typing import NamedTuple, List
from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()


class Cred6(NamedTuple):
    """Credit transaction that inherits from NamedTuple"""

    absolute_amount: float
    txn_type: str

    @property
    def amount(self):
        if self.txn_type == "DEBIT":
            return self.absolute_amount * -1
        else:
            return self.absolute_amount

    @classmethod
    def from_row(cls, row):
        return cls(absolute_amount=row[1], txn_type=row[2])

    @property
    def is_debit(self) -> bool:
        return self.txn_type == "DEBIT"


credits = [Cred6.from_row(r) for r in rows]
credit2 = credits[0]


class Order(NamedTuple):
    uid: int
    order_id: int
    order_type: str
    is_late: bool


class Order:
    def __init__(self, uid, order_id, order_type, is_late):
        self.uid = uid
        self.order_id = order_id
        self.order_type = order_type
        self.is_late = is_late
