

============================================================
TEST CASES — SCWP_11
============================================================

assert add_time("3:00 PM", "3:10") == "6:10 PM"
assert add_time("11:30 AM", "3:32", "Monday") == "3:02 PM, Monday"
assert add_time("11:43 PM", "24:20", "tuesday") == "12:03 AM, Wednesday (next day)"
assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"
assert add_time("8:16 PM", "466:02", "tuesday") == "6:18 AM, Monday (20 days later)"
assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)"

# Weekday rollover at exactly one day.
assert add_time("12:00 AM", "24:00", "Monday") == "12:00 AM, Tuesday (next day)"

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
