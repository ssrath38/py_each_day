"""
SCWP_10 — Learn Data Structures by Building the Merge Sort Algorithm

TARGET API
----------
merge_sort(array)

IMPORTANT COURSE CONTRACT
-------------------------
The list is sorted IN PLACE and `merge_sort()` returns `None`.

PROBLEM
-------
Implement merge sort using divide and conquer.

REQUIREMENTS
------------
1. Recursively split the list into smaller lists.
2. Recursively sort each half.
3. Merge the sorted halves back into the original list.
4. Do not call `sort()` or `sorted()`.
5. Handle empty lists and one-element lists.
6. Preserve duplicate values.
7. The intended time complexity is O(n log n).
8. Modify the original list object instead of returning a new sorted list.

EXAMPLE
-------
values = [5, 2, 4, 1]
result = merge_sort(values)

After the call:
    values == [1, 2, 4, 5]
    result is None
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    values = [5, 2, 4, 1]
    original = values
    result = merge_sort(values)
    assert values == [1, 2, 4, 5]
    assert result is None
    assert values is original

    values = []
    assert merge_sort(values) is None
    assert values == []

    values = [3, 3, 1, 2, 1]
    merge_sort(values)
    assert values == [1, 1, 2, 3, 3]

    values = [-4, 8, 0, -1, 3]
    merge_sort(values)
    assert values == [-4, -1, 0, 3, 8]
    print("SCWP_10 tests passed.")

if __name__ == "__main__":
    run_tests()
