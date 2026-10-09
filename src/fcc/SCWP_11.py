"""
SCWP_11 — Certification Project: Time Calculator

TARGET API
----------
add_time(start, duration, start_day=None)

PROBLEM
-------
Add a duration to a 12-hour clock time and report the resulting time, with day
information when requested.

REQUIREMENTS
------------
1. `start` uses the form H:MM AM or H:MM PM.
2. `duration` uses H:MM and may represent more than 24 hours.
3. Return the resulting time in 12-hour format with AM/PM.
4. Correctly handle crossing midnight.
5. If `start_day` is given, include the resulting weekday.
6. Day names are case-insensitive.
7. If one calendar day has passed, add `(next day)`.
8. If multiple calendar days have passed, add `(N days later)`.
9. Implement the arithmetic yourself rather than delegating the whole problem
   to a date/time helper.

EXAMPLES
--------
add_time("3:00 PM", "3:10")
    -> "6:10 PM"

add_time("11:30 AM", "3:32", "Monday")
    -> "3:02 PM, Monday"

add_time("11:43 PM", "24:20", "tuesday")
    -> "12:03 AM, Thursday"
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    assert add_time("3:00 PM", "3:10") == "6:10 PM"
    assert add_time("11:30 AM", "3:32", "Monday") == "3:02 PM, Monday"
    assert add_time("11:43 PM", "24:20", "tuesday") == "12:03 AM, Thursday (2 days later)"
    print("SCWP_11 tests passed.")

if __name__ == "__main__":
    run_tests()
