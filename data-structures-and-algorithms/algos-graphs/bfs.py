# This file completed with AI
from typing import List, Any, Dict


def breadth_first_search(graph: Dict[Any, List[Any]], start_vertex: Any) -> List[Any]:
    """
    Performs a breadth-first search (BFS) traversal on the given graph.

    Args:
        graph (Dict[Any, List[Any]]): The graph as an adjacency list.
        start_vertex (Any): The vertex from which to start the BFS.

    Returns:
        List[Any]: A list of vertices in the order they were visited.
    """
    visited: List[Any] = []
    unvisited: List[Any] = [start_vertex]  # Queue initialized with the starting vertex


    while unvisited:
        current = unvisited.pop(0)
        if current not in visited:
            visited.append(current)
            neighbors = sorted(graph.get(current, []))
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in unvisited:
                    unvisited.append(neighbor)
    return visited


""" Example Graph Representation
A-B-C-D
| | | |
E-F-G-H
| |   |
I-J   K
|
L
"""

# --- Example Usage ---
graph = {
    "A": ["B", "E"],
    "B": ["A", "C", "F"],
    "C": ["B", "D", "G"],
    "D": ["C", "H"],
    "E": ["A", "F", "I"],
    "F": ["B", "E", "G", "J"],
    "G": ["C", "F", "H"],
    "H": ["D", "G", "K"],
    "I": ["E", "J", "L"],
    "J": ["F", "I"],
    "K": ["H"],
    "L": ["I"]
}

result = breadth_first_search(graph, "A")
print("BFS Visit Order:", result)
