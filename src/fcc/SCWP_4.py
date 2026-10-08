

============================================================
TEST CASES — SCWP_4
============================================================

assert convert_to_snake_case("IAmAPascalCasedString") == "i_am_a_pascal_cased_string"
assert convert_to_snake_case("aLongAndComplexString") == "a_long_and_complex_string"
assert convert_to_snake_case("hello") == "hello"
assert convert_to_snake_case("Hello") == "hello"
assert convert_to_snake_case("Already") == "already"
assert convert_to_snake_case("") == ""

"""
SCWP_4 — Learn Python List Comprehensions by Building a Case Converter

TARGET API
----------
convert_to_snake_case(pascal_or_camel_cased_string)

PROBLEM
-------
Convert a PascalCase or camelCase string to snake_case.

REQUIREMENTS
------------
1. Process the string one character at a time.
2. When a character is uppercase, put an underscore before its lowercase form.
3. Lowercase characters remain lowercase.
4. Do not leave a leading or trailing underscore.
5. Use a list comprehension as part of the implementation.
6. Return the converted snake_case string.

EXAMPLES
--------
convert_to_snake_case("IAmAPascalCasedString")
    -> "i_am_a_pascal_cased_string"

convert_to_snake_case("aLongAndComplexString")
    -> "a_long_and_complex_string"
