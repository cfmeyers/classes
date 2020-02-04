from datetime import datetime, timedelta
from typing import List, Tuple


def get_credit_txn_rows_from_db() -> List[Tuple]:
    """
    simulate getting rows from a sql database

    Returns list of tuples:
        (uid, amount, txn_type, created_at, is_referral_credit)
    """

    yesterday = (datetime.now() - timedelta(days=1)).date()
    last_week = datetime(2020, 1, 28).date()
    last_year = datetime(2019, 7, 5).date()
    return [
        (777, 100.0, "CREDIT", last_year, True),
        (777, 20.75, "DEBIT", yesterday, None),
        (777, 10.0, "CREDIT", last_week, False),
        (999, 18.75, "DEBIT", yesterday, None),
        (999, 10.0, "DEBIT", last_week, None),
        (999, 100.0, "CREDIT", last_year, False),
    ]
