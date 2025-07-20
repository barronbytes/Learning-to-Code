# Graph Traversal Algorithms

Traversal algorithms can be used on graphs. You can [read about graphs here](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/data-structures.md#graphs) if you need a refresher.
 
## Breadth-First Search (BFS): O(v + e) [🔝](#graph-traversal-algorithms)

This is a **layer-by-layer** traversal that visits a graph’s vertices in the order of their distance from a starting point. It explores all directly connected vertices before moving to the next layer. This makes BFS especially useful for finding the shortest path in unweighted graphs.

Here's a breakdown of the time complexity: [view code here](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/algos-graphs/bfs.py)

* `while` loop runs once per **vertex** → contributes to `O(v)`
* `for` loop runs over each **neighbor (i.e. edge)** → contributes to `O(e)`
* So, the total runtime is `O(v + e)` 

## Depth-First Search (DFS): O(v + e) [🔝](#graph-traversal-algorithms)

This is a **deep-dive** traversal that follows a path from the starting point as far as possible before backtracking. It explores a branch fully before moving to the next, making it useful for checking connectivity or detecting cycles in a graph.

This is a **deep-diving** traversal that explores as far as possible along a branch before backtracking. It is great for connectivity checks, cycle detection, and traversing all paths in a graph.

Here's a breakdown of the time complexity: [view code here](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/algos-graphs/dfs.py)

* `recursive call` on each **vertex** once → contributes to `O(v)`
* `for` loop runs over each **neighbor (i.e. edge)** → contributes to `O(e)`
* So, the total runtime is `O(v + e)`

## Choosing Between BFS vs DFS for Graphs [🔝](#graph-traversal-algorithms)

Graphs can vary in how they spread:

* **Horizontally** → many vertices connected at the same depth (many connections, few levels)
* **Vertically** → few branching connections at each step, but edges continue deeply (few connections, many levels)

Here's advice on which to choose:

| Graph Shape    | When to Use | Reason                                                           |
| -------------- | ----------- | ---------------------------------------------------------------- |
| **Horizontal** | DFS         | Avoids high memory use from many same-depth connections          |
| **Vertical**   | BFS         | Avoids deep recursion and guarantees shortest path if one exists |

*If the search space is **infinite**, then use **BFS**.*
