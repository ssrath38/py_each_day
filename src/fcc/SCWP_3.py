

============================================================
TEST CASES — SCWP_3
============================================================

expenses = []
add_expense(expenses, 25.0, "food")
add_expense(expenses, 10.0, "transport")
add_expense(expenses, 15.5, "food")

assert total_expenses(expenses) == 50.5
assert filter_expenses_by_category(expenses, "food") == [
    {"amount": 25.0, "category": "food"},
    {"amount": 15.5, "category": "food"},
]

# Empty collection
assert total_expenses([]) == 0
assert filter_expenses_by_category([], "food") == []

# Verify that a newly added expense is represented with the required keys.
test_expenses = []
add_expense(test_expenses, 7.5, "books")
assert test_expenses[0]["amount"] == 7.5
assert test_expenses[0]["category"] == "books"

"""
SCWP_3 — Learn Lambda Functions by Building an Expense Tracker

PROBLEM
-------
Build a small expense tracker using Python functions, lambda expressions,
`map()`, and `filter()`.

DATA MODEL
----------
An expense is represented by:
    {"amount": <number>, "category": <string>}

TARGET FUNCTIONS
----------------
add_expense(expenses, amount, category)
total_expenses(expenses)
filter_expenses_by_category(expenses, category)
display_expenses(expenses)

REQUIREMENTS
------------
1. `add_expense` adds a new expense dictionary to the collection.
2. `total_expenses` returns the sum of all expense amounts.
3. `filter_expenses_by_category` returns only entries matching the category.
4. Use lambda expressions meaningfully with `map()` and/or `filter()`.
5. `display_expenses` presents each expense's amount and category.
6. Keep the functions reusable rather than hard-coding one dataset.

EXAMPLE
-------
expenses = [
    {"amount": 25.0, "category": "food"},
    {"amount": 10.0, "category": "transport"},
    {"amount": 15.5, "category": "food"},
]

total_expenses(expenses) -> 50.5
filter_expenses_by_category(expenses, "food") -> the two food entries
