"""
SCWP_7 — Learn Regular Expressions by Building a Password Generator

TARGET API
----------
generate_password(
    length=16,
    nums=1,
    special_chars=1,
    uppercase=1,
    lowercase=1
)

PROBLEM
-------
Generate a random password that satisfies minimum counts for four character
categories.

REQUIREMENTS
------------
1. `length` is the total password length.
2. `nums` is the minimum number of digits.
3. `special_chars` is the minimum number of punctuation/special characters.
4. `uppercase` is the minimum number of uppercase letters.
5. `lowercase` is the minimum number of lowercase letters.
6. Use letters, digits, and punctuation as the available character pool.
7. Use regular expressions to verify that the generated password satisfies
   each requested minimum.
8. Keep generating until all requested constraints are satisfied.
9. The result must have exactly the requested length.
10. Do not hard-code a password.

EXAMPLE
-------
generate_password(length=12, nums=2, special_chars=2,
                  uppercase=1, lowercase=1)

The returned string must have length 12 and satisfy all four minimum counts.
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    import string
    password = generate_password(length=16, nums=2, special_chars=2, uppercase=2, lowercase=2)
    assert len(password) == 16
    assert sum(c.isdigit() for c in password) >= 2
    assert sum(c.isupper() for c in password) >= 2
    assert sum(c.islower() for c in password) >= 2
    assert sum(c in string.punctuation for c in password) >= 2
    print("SCWP_7 tests passed.")

if __name__ == "__main__":
    run_tests()
