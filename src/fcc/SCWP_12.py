

============================================================
TEST CASES — SCWP_12
============================================================

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9],
]

board = Board(puzzle)
assert board.solver() is True
assert board.board == solution
assert board.find_empty_cell() is None

# An already-solved board should remain solved.
solved_board = Board(solution)
assert solved_board.solver() is True
assert solved_board.board == solution

# A known impossible board should return False rather than produce an invalid
# solution. Create a contradiction by placing two 5s in the first row.
bad = [row[:] for row in puzzle]
bad[0][2] = 5
bad_board = Board(bad)
assert bad_board.solver() is False

"""
SCWP_12 — Learn Classes and Objects by Building a Sudoku Solver

TARGET COMPONENTS
-----------------
class Board
solve_sudoku(board)

BOARD FORMAT
------------
A 9x9 list of lists.
- 0 means an empty cell.
- 1..9 are filled cells.

REQUIRED BOARD METHODS
----------------------
__str__()
find_empty_cell()
valid_in_row(row, num)
valid_in_col(col, num)
valid_in_square(row, col, num)
is_valid(empty, num)
solver()

PROBLEM
-------
Create an object-oriented Sudoku board and solve it with backtracking.

REQUIREMENTS
------------
1. `find_empty_cell` finds an empty cell or indicates that no empty cell remains.
2. A candidate is valid only when it does not already appear in its row,
   column, or 3x3 square.
3. `solver()` uses recursive backtracking:
   - choose an empty cell;
   - try a candidate 1..9;
   - recurse;
   - undo the guess when it leads to a dead end.
4. `solver()` returns True when solved and False when unsolvable.
5. `__str__()` renders the board and represents empty cells with `*`.
6. `solve_sudoku(board)` creates the Board and attempts the solve.

EDGE CASE
---------
An unsolvable puzzle must not be reported as solved.
