"""
SCWP_9 — Learn Recursion by Solving the Tower of Hanoi Puzzle

TARGET FUNCTION
---------------
move(n, source, auxiliary, target)

PROBLEM
-------
Solve Tower of Hanoi recursively while moving disk values between three rod
lists.

COURSE-STYLE SETUP
------------------
A is the source rod, B is the auxiliary rod, and C is the target rod.
Example initial state:
    rods = {
        "A": [3, 2, 1],
        "B": [],
        "C": []
    }

REQUIREMENTS
------------
1. Use recursion.
2. Move n-1 disks from source to auxiliary.
3. Move the remaining disk from source to target by popping from the source
   and appending to the target.
4. Print/display the rod configuration after each actual disk move.
5. Move the n-1 disks from auxiliary to target.
6. Never place a larger disk on top of a smaller disk.
7. Preserve the rod state using list operations.

ACCEPTANCE TEST
---------------
For n=3:
- exactly 7 disk moves must occur;
- all disks must finish on rod C;
- the final state must obey the size ordering.
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    source = [3, 2, 1]
    auxiliary = []
    target = []
    move(3, source, auxiliary, target)
    assert source == []
    assert sorted(target) == [1, 2, 3]
    assert len(target) == 3
    print("SCWP_9 tests passed.")

if __name__ == "__main__":
    run_tests()
