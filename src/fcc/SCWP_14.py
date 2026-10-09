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
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    food = Category("Food")
    food.deposit(100, "starting funds")
    assert food.get_balance() == 100
    assert food.withdraw(20, "groceries") is True
    assert food.get_balance() == 80
    assert food.withdraw(1000, "too much") is False
    assert food.get_balance() == 80

    transport = Category("Transport")
    assert food.transfer(30, transport) is True
    assert food.get_balance() == 50
    assert transport.get_balance() == 30
    chart = create_spend_chart([food, transport])
    assert chart.startswith("Percentage spent by category")
    print("SCWP_14 tests passed.")

if __name__ == "__main__":
    run_tests()
