# Graph Traversal Algorithms

Traversal algorithms can be used on graphs. You can [read about graphs here](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/data-structures.md#graphs) if you need a refresher.
 
## Breadth-First Search (BFS): O(n + e) [🔝](#graphs)

This is a **layer-by-layer** traversal that visits a graph’s vertices in the order of their distance from a starting point. It explores all direct neighbors before moving on to neighbors of neighbors, making it ideal for finding the shortest path in unweighted graphs.

Here's a breakdown of the time complexity: [view code here](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/algos-graphs/dfs.py)

* The `while` loop handles **discovery of each vertex** (think **"n"** for number of nodes)  
* The inner logic processes **edges from each vertex** (think **"e"** for total edges)  
* Combined, the overall complexity is **O(n + e)**  

## Depth-First Search (DFS): O(n + e) [🔝](#graphs)

This is a **deep-dive** traversal that follows a path from the starting point as far as possible before backtracking. It explores a branch fully before moving to the next, making it useful for checking connectivity or detecting cycles in a graph.

Here's a breakdown of the time complexity: [view code here](#)

* Each **node** is visited once (think **"n"** for vertices)  
* Each **edge** is explored once (think **"e"** for connections)  
* So, the total runtime is **O(n + e)**  
