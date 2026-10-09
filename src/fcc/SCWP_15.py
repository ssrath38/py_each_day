"""
SCWP_15 — Learn Special Methods by Building a Vector Space

TARGET COMPONENTS
-----------------
class R2Vector
class R3Vector

PROBLEM
-------
Implement 2D and 3D vector objects using Python special methods.

R2Vector REQUIRED BEHAVIOR
--------------------------
- `norm()`
- `__str__()`
- `__repr__()`
- `__add__()`
- `__sub__()`
- `__mul__()`
- `__eq__()`
- `__ne__()`
- `__lt__()`
- `__gt__()`
- `__le__()`
- `__ge__()`

REQUIREMENTS
------------
1. Store x and y components.
2. Vector + vector performs component-wise addition.
3. Vector - vector performs component-wise subtraction.
4. Vector * scalar performs scalar multiplication.
5. Vector * vector performs a dot product.
6. Comparisons use vector norm/magnitude.
7. String and repr output identify the components in the project's format.
8. Unsupported operand types should be handled appropriately.

R3Vector
--------
1. Extend R2Vector with a z component.
2. Preserve inherited operations in 3D.
3. Add `cross(other)` returning an R3Vector.

EXAMPLES
--------
R2Vector(x=1, y=2) + R2Vector(x=3, y=4)
    -> a vector representing (4, 6)

R2Vector(x=1, y=2) * R2Vector(x=3, y=4)
    -> 11

R3Vector(x=1, y=0, z=0).cross(R3Vector(x=0, y=1, z=0))
    -> R3Vector(x=0, y=0, z=1)
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    a = R2Vector(x=1, y=2)
    b = R2Vector(x=3, y=4)
    assert a + b == R2Vector(x=4, y=6)
    assert a - b == R2Vector(x=-2, y=-2)
    assert a * 3 == R2Vector(x=3, y=6)
    assert a * b == 11

    x_axis = R3Vector(x=1, y=0, z=0)
    y_axis = R3Vector(x=0, y=1, z=0)
    assert x_axis.cross(y_axis) == R3Vector(x=0, y=0, z=1)
    print("SCWP_15 tests passed.")

if __name__ == "__main__":
    run_tests()
