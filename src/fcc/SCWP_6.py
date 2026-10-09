"""
SCWP_6 — Certification Project: Arithmetic Formatter

TARGET API
----------
arithmetic_arranger(problems, show_answers=False)

PROBLEM
-------
Format up to five elementary addition/subtraction problems as a school-style
worksheet.

REQUIREMENTS
------------
1. Input examples look like "32 + 698" or "3801 - 2".
2. Only `+` and `-` are allowed.
3. More than five problems must return:
   "Error: Too many problems."
4. Any other operator must return:
   "Error: Operator must be '+' or '-'."
5. Non-digit operands must return:
   "Error: Numbers must only contain digits."
6. Operands longer than four digits must return:
   "Error: Numbers cannot be more than four digits."
7. Right-align the two operands.
8. Put two spaces between the operator and the second operand.
9. Put four spaces between adjacent problems.
10. Underline each problem with dashes.
11. When `show_answers=True`, add the calculation results on a fourth line.
12. Return one final string with the exact worksheet spacing.
13. Do not add trailing spaces to any output line.

EXAMPLE
-------
arithmetic_arranger(
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
)

The returned value must be correctly aligned and contain the expected answer
line when `show_answers` is enabled.
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    assert arithmetic_arranger(["3 + 855"]) == "    3\n+ 855\n-----"
    assert arithmetic_arranger(["3 + 855"], True) == "    3\n+ 855\n-----\n  858"
    assert arithmetic_arranger(["3 * 5"]) == "Error: Operator must be '+' or '-'."
    assert arithmetic_arranger(["12345 + 1"]) == "Error: Numbers cannot be more than four digits."
    assert arithmetic_arranger(["1 + 2"] * 6) == "Error: Too many problems."
    print("SCWP_6 tests passed.")

if __name__ == "__main__":
    run_tests()
