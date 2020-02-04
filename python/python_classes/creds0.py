from helpers import get_credit_txn_rows_from_db

rows = get_credit_txn_rows_from_db()

##
##
##
##
##
##
##
##
##
##

total = 0.0
for row in rows:
    if row[2] == "CREDIT":
        total += row[1]  # amount
    else:
        total -= row[1]  # amount
print(total)


row = rows[0]
