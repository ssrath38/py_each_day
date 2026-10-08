

============================================================
TEST CASES — SCWP_16
============================================================

linear = LinearEquation(2, 3)
roots = linear.solve()
assert len(roots) == 1
assert abs(roots[0] + 1.5) < 1e-9

analysis = linear.analyze()
assert analysis["slope"] == -1.5
assert analysis["intercept"] == 0

quadratic = QuadraticEquation(1, -3, 2)
roots = quadratic.solve()
assert sorted(roots) == [1, 2]

quadratic_one = QuadraticEquation(1, -2, 1)
assert quadratic_one.solve() == [1.0]

quadratic_none = QuadraticEquation(1, 0, 1)
assert quadratic_none.solve() == []

# Vertex of x^2 - 4x + 3 is (2, -1), with a minimum.
vertex_info = QuadraticEquation(1, -4, 3).analyze()
assert abs(vertex_info["vertex"][0] - 2) < 1e-9
assert abs(vertex_info["vertex"][1] + 1) < 1e-9

# Leading coefficient zero should be rejected.
# LinearEquation(0, 3)
# QuadraticEquation(0, 1, 2)

# solver() should reject unrelated objects.
# solver("x + 1")

"""
SCWP_16 — Learn Interfaces by Building an Equation Solver

TARGET COMPONENTS
-----------------
Equation (abstract base class)
LinearEquation
QuadraticEquation
solver(equation)

PROBLEM
-------
Build an equation-solving interface using an abstract base class and concrete
equation implementations.

Equation
--------
1. Declare an abstract base class named `Equation`.
2. Concrete subclasses provide `degree` and `type`.
3. Accept exactly `degree + 1` numeric coefficients.
4. The leading coefficient must not be zero.
5. Provide abstract `solve()` and `analyze()` methods.
6. Format the polynomial in `__str__()`.

LinearEquation
--------------
Represents:
    ax + b = 0

Requirements:
- `solve()` returns the real root in a list.
- `analyze()` returns slope and intercept information.

QuadraticEquation
-----------------
Represents:
    ax^2 + bx + c = 0

Requirements:
- compute the discriminant;
- return [] for no real roots;
- return one root for a zero discriminant;
- return two roots for two distinct real roots;
- `analyze()` reports the vertex and whether the parabola has a minimum or
  maximum, together with concavity.

solver(equation)
----------------
1. Accept an Equation instance.
2. Produce a fixed-width, formatted report containing the equation, its type,
   solutions, and analysis.
3. Reject objects that are not equation instances.

EXAMPLE
-------
LinearEquation(2, 3) represents:
    2x + 3 = 0

Its solution is:
    x = -1.5
