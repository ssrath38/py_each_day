

============================================================
TEST CASES — SCWP_7
============================================================

import re

password = generate_password(12, 2, 2, 2, 2)
assert len(password) == 12
assert len(re.findall(r"\d", password)) >= 2
assert len(re.findall(r"[A-Z]", password)) >= 2
assert len(re.findall(r"[a-z]", password)) >= 2
assert len(re.findall(r"[^A-Za-z0-9]", password)) >= 2

password = generate_password(8, 0, 0, 0, 8)
assert len(password) == 8
assert password.isalpha() and password.islower()

# The generated password should satisfy the defaults.
default_password = generate_password()
assert len(default_password) == 16
assert re.search(r"\d", default_password)
assert re.search(r"[A-Z]", default_password)
assert re.search(r"[a-z]", default_password)
assert re.search(r"[^A-Za-z0-9]", default_password)

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
