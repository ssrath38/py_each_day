

============================================================
TEST CASES — SCWP_18
============================================================

projectile = Projectile(10, 5, 45)
assert projectile.speed == 10
assert projectile.height == 5
assert projectile.angle == 45

projectile.speed = 20
assert projectile.speed == 20
projectile.height = 10
assert projectile.height == 10
projectile.angle = 30
assert projectile.angle == 30

# The initial point should be the launch height.
coords = projectile.calculate_all_coordinates()
assert coords
assert coords[0][0] == 0
assert abs(coords[0][1] - projectile.height) < 1e-9

# The trajectory should eventually reach/approach y = 0.
assert min(y for _, y in coords) <= projectile.height

# A formatted coordinates table and trajectory must be strings.
graph = Graph(coords)
assert isinstance(graph.create_coordinates_table(), str)
assert isinstance(graph.create_trajectory(), str)

# Invalid physical inputs should be rejected according to your validation
# policy, for example a negative speed or invalid height.
# Projectile(-10, 5, 45)

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
