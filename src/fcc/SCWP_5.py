"""
SCWP_5 — Learn the Bisection Method by Finding the Square Root of a Number

TARGET API
----------
square_root_bisection(square_target, tolerance=1e-7, max_iterations=100)

PROBLEM
-------
Approximate the real square root of a non-negative number using the bisection
method. Do not use `math.sqrt()`.

REQUIREMENTS
------------
1. For a negative input, raise:
   ValueError("Square root of negative number is not defined in real numbers")
2. For 0 and 1, return the exact value and print the course-style message.
3. For other positive values, maintain lower/upper bounds that contain the
   root and repeatedly bisect the interval.
4. Update the bounds according to whether `midpoint**2` is below or above
   the target.
5. Stop when the square error is within `tolerance`.
6. Stop after `max_iterations` attempts.
7. If the method does not converge, print:
   Failed to converge within <max_iterations> iterations.
   and return `None`.
8. On success, return the approximation and print the course-style result.

EXAMPLES
--------
square_root_bisection(16) -> approximately 4.0
square_root_bisection(2)  -> approximately 1.41421356
square_root_bisection(0)  -> 0
square_root_bisection(1)  -> 1
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    assert abs(square_root_bisection(16) - 4.0) < 1e-6
    assert abs(square_root_bisection(2) ** 2 - 2) < 1e-6
    assert square_root_bisection(0) == 0
    assert square_root_bisection(1) == 1
    try:
        square_root_bisection(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("A negative target should raise ValueError.")
    print("SCWP_5 tests passed.")

if __name__ == "__main__":
    run_tests()
