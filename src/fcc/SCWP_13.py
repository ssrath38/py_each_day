

============================================================
TEST CASES — SCWP_13
============================================================

tree = BinarySearchTree()
for value in [50, 30, 20, 40, 70, 60, 80]:
    tree.insert(value)

assert tree.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]
assert tree.search(40) is not None
assert tree.search(999) is None

# Delete a leaf.
tree.delete(20)
assert tree.inorder_traversal() == [30, 40, 50, 60, 70, 80]

# Delete a node with one child.
tree.insert(65)
tree.delete(60)
assert tree.inorder_traversal() == [30, 40, 50, 65, 70, 80]

# Delete a node with two children.
tree.delete(70)
assert tree.inorder_traversal() == [30, 40, 50, 65, 80]

# Duplicate insertion must not create a second node.
tree.insert(50)
assert tree.inorder_traversal().count(50) == 1

# Delete the root and verify the tree is still ordered.
tree.delete(50)
assert tree.inorder_traversal() == [30, 40, 65, 80]

"""
SCWP_13 — Learn Tree Traversal by Building a Binary Search Tree

TARGET COMPONENTS
-----------------
class TreeNode
class BinarySearchTree

PROBLEM
-------
Implement a binary search tree with insertion, search, deletion, and inorder
traversal.

REQUIREMENTS
------------
1. `TreeNode` stores a key plus left and right child references.
2. `BinarySearchTree` starts with `root = None`.
3. `insert(key)` recursively inserts smaller keys left and larger keys right.
4. Do not create a second node for a duplicate key.
5. `search(key)` returns the matching node or None.
6. `delete(key)` handles all three cases:
   - leaf;
   - one child;
   - two children.
7. For two children, replace the deleted value using an appropriate successor
   and repair the tree recursively.
8. `inorder_traversal()` returns values in ascending order.
9. Use recursive helper methods where needed.

EXAMPLE
-------
Insert:
    50, 30, 20, 40, 70, 60, 80

Inorder:
    [20, 30, 40, 50, 60, 70, 80]

Delete 40 and verify that inorder no longer contains 40 and the BST property
still holds.
