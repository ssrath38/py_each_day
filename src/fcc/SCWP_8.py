

============================================================
TEST CASES — SCWP_8
============================================================

graph = {
    "A": [("B", 3), ("C", 1)],
    "B": [("A", 3), ("C", 1)],
    "C": [("A", 1), ("B", 1)],
}
distances, paths = shortest_path(graph, "A")
assert distances["A"] == 0
assert distances["B"] == 2
assert distances["C"] == 1
assert paths["B"] == ["A", "C", "B"]
assert paths["C"] == ["A", "C"]

# Disconnected node must remain unreachable.
graph2 = {
    "A": [("B", 1)],
    "B": [("A", 1)],
    "C": [],
}
distances, paths = shortest_path(graph2, "A")
assert "C" not in distances or distances["C"] == float("inf")

# A direct edge should beat a longer indirect route.
graph3 = {
    "A": [("B", 10), ("C", 2)],
    "C": [("B", 3)],
    "B": [],
}
distances, paths = shortest_path(graph3, "A")
assert distances["B"] == 5
assert paths["B"] == ["A", "C", "B"]

"""
SCWP_8 — Learn Algorithm Design by Building a Shortest Path Algorithm

TARGET API
----------
shortest_path(graph, start, target='')

GRAPH FORMAT
------------
graph = {
    node: [(neighbor, distance), ...],
    ...
}

PROBLEM
-------
Implement Dijkstra's shortest-path algorithm for a graph with non-negative
edge weights.

REQUIREMENTS
------------
1. Start from `start`.
2. Track the current best known distance to every reachable node.
3. Repeatedly select the unvisited node with the smallest current distance.
4. Relax its outgoing edges.
5. Track predecessors/path information so actual shortest paths can be rebuilt.
6. Return:
       (distances, paths)
7. `distances` maps nodes to their shortest distance from `start`.
8. `paths` maps nodes to the corresponding node sequence.
9. A target value may be supplied for a focused lookup; the course contract
   still returns the distance/path structures.
10. Do not use a third-party graph library.

EXAMPLE
-------
graph = {
    "A": [("B", 3), ("C", 1)],
    "B": [("A", 3), ("C", 1)],
    "C": [("A", 1), ("B", 1)],
}

The shortest path A -> B is A -> C -> B with total distance 2.
