

============================================================
TEST CASES — SCWP_19
============================================================

hat = Hat(black=6, red=4, green=3)
assert len(hat.contents) == 13
assert hat.contents.count("black") == 6
assert hat.contents.count("red") == 4
assert hat.contents.count("green") == 3

# Drawing fewer balls must remove exactly that many balls.
drawn = hat.draw(5)
assert len(drawn) == 5
assert len(hat.contents) == 8

# A fresh hat with fewer balls than requested should return all remaining balls.
small = Hat(red=2)
drawn = small.draw(5)
assert sorted(drawn) == ["red", "red"]
assert small.contents == []

# Probability 1: every trial must contain all balls when exactly all balls are
# drawn and the expected count matches the complete hat.
certain = Hat(red=2)
assert experiment(certain, {"red": 2}, 2, 25) == 1.0

# A probability must always be between 0 and 1.
normal = Hat(black=6, red=4, green=3)
probability = experiment(normal, {"red": 2, "green": 1}, 5, 100)
assert 0.0 <= probability <= 1.0

"""
SCWP_19 — Certification Project: Probability Calculator

TARGET COMPONENTS
-----------------
class Hat
experiment(hat, expected_balls, num_balls_drawn, num_experiments)

PROBLEM
-------
Estimate the probability of drawing a requested combination of colored balls
from a hat using repeated random experiments without replacement.

Hat
---
Initialize with keyword counts, for example:
    Hat(black=6, red=4, green=3)

The hat's `contents` must contain one color string for each individual ball.

Required method
---------------
draw(num_balls)

REQUIREMENTS FOR draw()
-----------------------
1. Remove balls randomly.
2. Draw without replacement.
3. Return the drawn colors as a list.
4. If more balls are requested than remain, return all remaining balls.

EXPERIMENT
----------
experiment(hat, expected_balls, num_balls_drawn, num_experiments)

1. Run the requested number of independent trials.
2. Each trial must start from a separate copy of the original hat.
3. Draw `num_balls_drawn` balls.
4. Count the occurrences of each color.
5. A trial succeeds only when the sample contains at least the requested
   number of every color in `expected_balls`.
6. Return:
       successful_experiments / num_experiments
7. Do not hard-code an expected probability.

EXAMPLE
-------
hat = Hat(black=6, red=4, green=3)
expected_balls = {"red": 2, "green": 1}

Estimate the probability of drawing 5 balls containing at least 2 red and at
least 1 green ball.
