

============================================================
TEST CASES — SCWP_14
============================================================

food = Category("Food")
food.deposit(1000, "initial deposit")
assert food.get_balance() == 1000

assert food.withdraw(100, "groceries") is True
assert food.get_balance() == 900
assert food.check_funds(900) is True
assert food.check_funds(901) is False
assert food.withdraw(901, "too much") is False
assert food.get_balance() == 900

entertainment = Category("Entertainment")
entertainment.deposit(500, "payday")
assert food.transfer(200, entertainment) is True
assert food.get_balance() == 700
assert entertainment.get_balance() == 700
assert food.transfer(1000, entertainment) is False

# String representation should contain the category heading, descriptions,
# and total balance using the required 30-character formatting.
text = str(food)
assert "Food" in text
assert "Total:" in text
assert "groceries" in text

# Spending chart with one category: only that category has spending.
chart = create_spend_chart([food])
assert "Percentage spent by category" in chart
assert "F" in chart

# A category with no withdrawals should still be supported.
empty = Category("Empty")
chart = create_spend_chart([empty])
assert "Percentage spent by category" in chart

"""
SCWP_14 — Certification Project: Budget App

TARGET COMPONENTS
-----------------
class Category
create_spend_chart(categories)

PROBLEM
-------
Build a category-based budget ledger.

Category API
------------
__init__(name)
deposit(amount, description="")
withdraw(amount, description="")
get_balance()
transfer(amount, destination_category)
check_funds(amount)
__str__()

REQUIREMENTS
------------
1. Store the category name and a ledger list.
2. Each ledger entry contains amount and description.
3. Deposits add positive amounts.
4. Withdrawals subtract amounts only when sufficient funds exist and return
   True on success, otherwise False.
5. `get_balance()` returns the sum of ledger amounts.
6. `check_funds(amount)` reports whether enough money is available.
7. A successful transfer subtracts from the source and deposits into the
   destination with the required descriptions.
8. `__str__()` formats the title, ledger entries, and total using the project's
   30-character layout.
9. `create_spend_chart(categories)` considers withdrawals only.
10. Each category's spending percentage is based on its withdrawals divided by
    total withdrawals across all categories.
11. Render the chart vertically from 100 down to 0 and label the categories at
    the bottom.
12. Exact spacing in the returned strings matters for the certification tests.
