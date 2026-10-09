"""
SCWP_17 — Certification Project: Polygon Area Calculator

TARGET COMPONENTS
-----------------
class Rectangle
class Square

Rectangle API
-------------
__init__(width, height)
set_width(width)
set_height(height)
get_area()
get_perimeter()
get_diagonal()
get_picture()
get_amount_inside(shape)

Square API
----------
__init__(side)
set_side(side)
set_width(width)
set_height(height)

PROBLEM
-------
Use inheritance to model rectangles and squares.

REQUIREMENTS
------------
1. Rectangle stores width and height.
2. `get_area()` returns width * height.
3. `get_perimeter()` returns 2*width + 2*height.
4. `get_diagonal()` returns the geometric diagonal.
5. `get_picture()` renders the shape using `*`, with one row per height unit.
6. If either dimension is greater than 50, return:
   "Too big for picture."
7. `get_amount_inside(shape)` counts how many whole copies of another shape
   fit inside without rotation.
8. Square subclasses Rectangle.
9. A Square's width and height must always remain equal.
10. `set_side`, `set_width`, and `set_height` must preserve square shape.
11. Match the course's string representations and spacing.

EXAMPLE
-------
Rectangle(10, 8).get_amount_inside(Square(2))
    -> 20
"""

# TODO: Implement the required functions/classes above this test block.
def run_tests():
    rect = Rectangle(10, 5)
    assert rect.get_area() == 50
    assert rect.get_perimeter() == 30
    assert rect.get_picture() == ("**********\n" * 5)
    assert rect.get_amount_inside(Square(2)) == 10

    square = Square(4)
    square.set_width(5)
    assert square.width == 5 and square.height == 5
    print("SCWP_17 tests passed.")

if __name__ == "__main__":
    run_tests()
