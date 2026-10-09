"""
SCWP_2 — Work with Numbers and Strings by Implementing the Luhn Algorithm

TARGET API
----------
verify_card_number(card_number)

PROBLEM
-------
Implement the Luhn checksum test for a numeric string.

REQUIREMENTS
------------
1. Treat the input as a string so leading zeroes are preserved.
2. Starting from the right, process digits in alternating positions.
3. Add ordinary digits directly.
4. For every other digit, double it; if the doubled value has two digits,
   reduce it to the sum of its digits.
5. Add the resulting values.
6. Return `True` when the total is divisible by 10; otherwise return `False`.
7. Reject malformed non-numeric input instead of silently accepting it.

EXAMPLES
--------
verify_card_number("4532015112830366") -> True
verify_card_number("8273123273520569") -> False

CONSTRAINT
----------
Do not use a third-party Luhn implementation.
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    assert verify_card_number("4532015112830366") is True
    assert verify_card_number("8273123273520569") is False
    assert verify_card_number("12") is False
    print("SCWP_2 tests passed.")

if __name__ == "__main__":
    run_tests()
