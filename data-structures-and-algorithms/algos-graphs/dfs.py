# This file completed with AI
from typing import List, Any, Dict


def depth_first_search(graph: Dict[Any, List[Any]], start_vertex: Any) -> List[Any]:
    """
    Performs a depth-first search (DFS) traversal on the given graph.

    Args:
        graph (Dict[Any, List[Any]]): The graph as an adjacency list.
        start_vertex (Any): The vertex from which to start the DFS.

    Returns:
        List[Any]: A list of vertices in the order they were visited.
    """
    visited: List[Any] = []
    depth_first_search_r(graph, start_vertex, visited)
    return visited


def depth_first_search_r(graph: Dict[Any, List[Any]], current_vertex: Any, visited: List[Any]) -> None:
    """
    Recursive helper function for DFS traversal.

    Args:
        graph (Dict[Any, List[Any]]): The graph as an adjacency list.
        current_vertex (Any): The current vertex being visited.
        visited (List[Any]): The list of already visited vertices.
    """
    visited.append(current_vertex)
    neighbors = sorted(graph.get(current_vertex, []))
    for neighbor in neighbors:
        if neighbor not in visited:
            depth_first_search_r(graph, neighbor, visited)


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

result = depth_first_search(graph, "A")
print("DFS Visit Order:", result)
