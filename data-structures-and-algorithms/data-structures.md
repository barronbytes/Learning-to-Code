# Data Structures

Learning data structures is *super* hard! Building them from scratch turned out to be a great way to learn. I coded some on my own and leaned on AI for others—I'm looking at you, [Red-Black Tree](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/data-structures/my_red_black_tree.py)! 😅 These guiding questions helped me think through each one:

* What does it do?
* What is it needed for?
* What methods exist and what rules must be followed?
* What edge cases should I consider?
* What are the drawbacks to this data structure?
* What is the best and worst case time complexity for methods?

## 1. Stacks (LIFO)

### Purpose

A stack is a **linear data structure** that stores elements using the **Last In, First Out (LIFO)** principle. This means the last item added is the first one removed. Think of it like a stack of plates—add to the top, remove from the top.

**O(1)** operations for insertions/deletions at **top**:

* `value`
* `next` (pointer to next node)

### Use Cases

* Undo/redo functionality in text editors
* Managing browser history (back/forward)

### Drawbacks

* Limited access: can only access last (newest) element
* No direct access to first (oldest) and middle elements
* Inefficient for searching or accessing non-top elements

## 2. Queues (FIFO)

### Purpose

A queue is a **linear data structure** that stores elements using the **First In, First Out (FIFO)** principle. This means the first item added is the first one removed—like people lining up in a queue at a store: first in, first out.

**O(1)** operations for insertions at the **tail** and deletions at the **head**:

* `value`
* `next` (pointer to next node)

### Use Cases

* Task scheduling (e.g., print jobs, OS process management)
* Buffering data streams (e.g., I/O buffering, network packets)

### Drawbacks

* Limited access: can only access the front and rear elements
* No direct access to middle elements
* Not ideal for scenarios requiring frequent random access or reverse-order processing

## 3. Linked Lists

### Purpose

A linked list is a **linear data structure** where each element, called a **node**, stores both a value and a reference (or pointer) to another node. Two types of references exist. **Singly linked** pointers only track the next node. **Doubly linked** pointers track the previous and next node. You can think of this data structure as a treasure hunt where clues point to the next clue.

**O(1)** operations for insertions/deletions:

* `value`
* `next` (pointer to next node)
* `prev` (pointer to previous node)

### Use Cases

* Memory-constrained systems where dynamic allocation is preferred
* Implementing other data structures!!! (e.g. stacks, queues, hash tables, adjacency lists)

### Drawbacks

* O(n) time to access or search for an element
* No index-based access like arrays (`list[i]` won't work)
* Extra memory for next and previous pointers

## 4. Binary Trees

### Purpose

A binary tree is a **hierarchical data structure**. The structure branches out like a family tree, with one node connected to its descendants.

**O(log n)** operations for insertions, deletions, and search:

* `value`
* `left` (pointer to left child)
* `right` (pointe to right child)

### Use Cases

* Representing hierarchical data (e.g., file systems)
* Fast insertion, deletion, and search for balanced data

### Drawbacks

* O(n) for unbalanced trees
* Extra memory overhead left and right child pointers

## 5. Red-Black Trees

A red-black tree is a **self-balancing binary search tree**. It maintains balance through **color-based** rules and rotations.

**O(log n)** operations for insertions, deletions, and search:

* `value` (**no duplicates**)
* `left` (pointer to left child)
* `right` (pointe to right child)
* `color` (either red or black)
* `parent`(for easier rebalancing)
* `nil` (sentinal node used instead of `None`)

### Use Cases

* Databases and memory allocators where guaranteed balance is crucial
* Track file chagnes (e.g. version control systems)

### Drawbacks

* Complex implementation due to balancing rules and rotations
* Extra memory for storing node color and sometimes parent pointers
