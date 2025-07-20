# This file completed with AI
from typing import Any, Set, Dict


class Graph:
    """
    Graph class (undirected, unweighted).

    Core Methods: __init__(), add_vertex(), add_edge(), adjacent_vertices(), edge_exists()
    Internal Helpers: _ensure_vertex()

    Representation:
    - Adjacency List: Dict[vertex] → Set of connected vertices
    - Automatically adds missing vertices when creating edges
    - Supports any hashable type for vertex (int, str, etc.)
    """
    def __init__(self) -> None:
        # Initialize an empty dictionary to represent the adjacency list
        self.adj_list: Dict[Any, Set[Any]] = {}


    def add_vertex(self, vertex: Any) -> None:
        # Add vertex to graph if it does not already exist
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()


    def add_edge(self, u: Any, v: Any) -> None:
        # Add undirected edge between vertices u and v, auto-adding vertices if missing
        self._ensure_vertex(u)
        self._ensure_vertex(v)
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)


    def adjacent_vertices(self, vertex: Any) -> Set[Any]:
        # Return the set of adjacent vertices, or empty set if vertex is not in graph
        return self.adj_list.get(vertex, set())


    def edge_exists(self, u: Any, v: Any) -> bool:
        # Check if an edge exists between u and v
        return v in self.adj_list.get(u, set())


    def _ensure_vertex(self, vertex: Any) -> None:
        # Internal helper: create vertex if it doesn't exist
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()


# --- Example Usage ---
g = Graph()

# Add vertices
g.add_vertex(1)
g.add_vertex(2)

# Add edges (auto-adds vertex 3)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(1, 2)

# Adjacency queries
print("Neighbors of 1:", g.adjacent_vertices(1))   # {2, 3}
print("Neighbors of 3:", g.adjacent_vertices(3))   # {1, 2}
print("Neighbors of 9:", g.adjacent_vertices(9))   # set()

# Edge existence
print("Edge 1–2?:", g.edge_exists(1, 2))            # True
print("Edge 2–1?:", g.edge_exists(2, 1))            # True
print("Edge 1–9?:", g.edge_exists(1, 9))            # False
