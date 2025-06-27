# Data Structures and Algorithms

Each folder in this repository showcases steps taken along my learning journey.

## Big O Notation

This notation is a metric used to measure the following:

* Time Complexity: How much time an algorithm takes to run
* Space Complexity: How much memory an algorithm takes to run

<img src="assets/time_complexity.PNG" alt="Time Complexity Graphs" width="60%">

Time complexity analysis considers best-case, average-case, and worst-case scenarios. In business contexts, the worst-case is given the most importance. Below are common worst-case scenarios, ranked from most efficient to least efficient:

| **Big O Notation** | **Scenarios / Examples**                                                                  |
|--------------------|-------------------------------------------------------------------------------------------|
| **O(1)**           | - Accessing an element by index in an array or list                                       |
|                    | - Hash table/dictionary lookups                                                           |
|                    | - Pushing/popping from a stack or queue                                                   |
|                    | - Swapping two variables                                                                  |
| **O(log n)**       | - Binary search in a sorted array                                                         |
|                    | - Inserting/searching in a balanced binary search tree (e.g., AVL, Red-Black Tree)        |
|                    | - Operations on heaps (e.g., insert, delete-min in a binary heap)                         |
|                    | - Efficient searching in databases (e.g., B-trees)                                        |
| **O(n)**           | - Linear search in an unsorted list                                                       |
|                    | - Traversing all elements in an array or linked list                                      |
|                    | - Copying an array or string                                                              |
|                    | - Finding the maximum/minimum element in a list                                           |
| **O(n log n)**     | - Merge Sort, Heap Sort, and Quick Sort (average case)                                    |
|                    | - Building a binary heap                                                                  |
|                    | - Most efficient comparison-based sorting algorithms                                      |
|                    | - Fast Fourier Transform                                                                  |
| **O(n²)**          | - Bubble Sort, Insertion Sort, Selection Sort (worst cases)                               |
|                    | - Comparing all pairs in a list                                                           |
|                    | - Checking for duplicates using nested loops                                              |
|                    | - Simple dynamic programming with two dimensions (e.g., edit distance)                    |
| **O(n³)**          | - Triple nested loops (e.g., brute-force matrix multiplication)                           |
|                    | - Floyd-Warshall algorithm for all-pairs shortest paths                                   |
|                    | - Dynamic programming with three dimensions                                               |
| **O(2ⁿ)**          | - Solving the subset sum problem using recursion                                          |
|                    | - Recursive solutions to the Traveling Salesman Problem (TSP)                             |
|                    | - Generating all subsets of a set                                                         |
|                    | - Exponential recursive solutions without memoization                                     |
| **O(n!)**          | - Generating all permutations of a set                                                    |
|                    | - Brute-force solution to the Traveling Salesman Problem (TSP)                            |
|                    | - Solving puzzles like the n-queens problem with backtracking (worst case)                |
