

============================================================
TEST CASES — SCWP_9
============================================================

Use the same rod structure required by your implementation.

# n = 1
# One move should occur and disk 1 should end on C.
# moves = []
# move(1, A, B, C)
# assert A == [] and C == [1]

# n = 3
# Exactly 7 moves should occur.
# The final state must contain all disks on the target rod in valid order.
# assert len(recorded_moves) == 7
# assert A == [] and B == [] and C == [3, 2, 1]

# n = 4
# The minimum number of moves is 15.
# assert len(recorded_moves) == 15

# Edge case:
# move(0, A, B, C) should perform no disk move.

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
