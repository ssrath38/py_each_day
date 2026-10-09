"""
SCWP_18 — Learn Encapsulation by Building a Projectile Trajectory Calculator

TARGET COMPONENTS
-----------------
class Projectile
class Graph
projectile_helper(speed, height, angle)

Projectile
----------
Initialize with:
    Projectile(speed, height, angle)

Expose the main values through properties:
    speed
    height
    angle

PROBLEM
-------
Model projectile motion while keeping the projectile's internal state
encapsulated, then render the resulting coordinates as text.

REQUIREMENTS
------------
1. Keep the underlying speed, height, and angle values private.
2. Provide getters/setters through properties.
3. Use gravitational acceleration `9.81 m/s^2`.
4. Accept the launch angle in degrees; use radians internally for trigonometric
   calculations.
5. Compute the horizontal displacement when the projectile reaches ground level.
6. Compute the vertical coordinate for a supplied horizontal position.
7. `calculate_all_coordinates()` returns the trajectory as `(x, y)` pairs
   using the project's integer-x sampling approach.
8. `__str__()` reports the projectile parameters and horizontal displacement.
9. `__repr__()` identifies the object and its current properties.

Graph
-----
1. Initialize with the coordinate list.
2. Keep coordinate data encapsulated.
3. `create_coordinates_table()` returns a formatted x/y table.
4. `create_trajectory()` returns a text visualization of the trajectory.

Helper
------
`projectile_helper(speed, height, angle)` builds the projectile, calculates the
coordinates, builds the graph, and displays the course-style reports.
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    projectile = Projectile(10, 0, 45)
    assert projectile.speed == 10
    assert projectile.height == 0
    assert projectile.angle == 45
    coords = projectile.calculate_all_coordinates()
    assert isinstance(coords, list)
    assert len(coords) > 0
    assert isinstance(coords[0], tuple) and len(coords[0]) == 2
    print("SCWP_18 tests passed.")

if __name__ == "__main__":
    run_tests()
