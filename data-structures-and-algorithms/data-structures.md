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

**Average O(1)** operations for insertions/deletions at **top**:

* `value`
* `next` (pointer to next node)

### Use Cases

* Undo/redo functionality in text editors
* Managing browser history (back/forward)

### Drawbacks

* Limited access: can only access last (newest) element
* Stack operations are limited: no searching, no sorting, no random access
* Inefficient for searching or accessing non-top elements

## 2. Queues (FIFO)

### Purpose

A queue is a **linear data structure** that stores elements using the **First In, First Out (FIFO)** principle. This means the first item added is the first one removed—like people lining up in a queue at a store: first in, first out.

**Average O(1)** operations for insertions at the **tail** and deletions at the **head**:

* `value`
* `next` (pointer to next node)

### Use Cases

* Task scheduling (e.g., print jobs, OS process management)
* Buffering data streams (e.g., I/O buffering, network packets)

### Drawbacks

* Limited access: can only access the front and rear elements
* Queue operations are limited: no searching, no sorting, no random access
* Not ideal for scenarios requiring frequent random access or reverse-order processing

## 3. Linked Lists

### Purpose

A linked list is a **linear data structure** where each element, called a **node**, stores both a value and a reference (or pointer) to another node. Two types of references exist. **Singly linked** pointers only track the next node. **Doubly linked** pointers track the previous and next node. You can think of this data structure as a treasure hunt where clues point to the next clue.

**Average O(1)** operations for insertions/deletions:

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

**Average O(log n)** operations for insertions, deletions, and search:

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

**Average O(log n)** operations for insertions, deletions, and search:

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

## 6. HashMaps

A HashMap is an **associative array** data structure that stores key-value pairs and enables fast average-case lookups by using a hash function and collision resolution. Think of it like a library catalog where the key is the book’s title used to find the exact shelf (the index), and the value is the book itself located there.

**Average O(1)** operations for insertions, deletions, and search:

* `data` (array of buckets storing key-value pairs or None)  
* `size` (current capacity of the array)  
* `filled_count` (number of occupied buckets)  
* `hash function` (maps keys to indices)  
* `collision resolution` (commonly **linear probing** or chaining)  
- `load factor` (ratio of filled buckets to size to decide resizing)  

### Use Cases

* Implementing dictionaries or associative arrays in programming languages  
* Caching systems where fast key-value lookup is critical  
* Databases and indexing structures where quick retrieval matters  

### Drawbacks

* Performance degrades with poor hash functions or high load factors (> 0.70)
* Resizing can be costly in terms of time and memory
* Keys must be hashable and ideally evenly distributed for best performance

## 7. Tries

A trie is a **tree-based** data structure used to efficiently store and retrieve strings, especially when many share common prefixes. Think of it like an **autocomplete system**—each character of a word branches out like steps on a trail, and shared beginnings follow the same path.

**Average O(k)** time complexity for insertions, deletions, and search, where **k** is the length of the string:

* `root` (starting node; usually empty or null character)  
* `nodes` (each stores one character and links to child nodes)  
* `children` (map from character to child node)  
* `is_end` (boolean flag to mark end of a valid word)  
* `insert(word)` (adds each character one by one)  
* `search(word)` (traces path for the full word)  
* `starts_with(prefix)` (checks if any word starts with the prefix)

### Use Cases

* Autocomplete systems and search engines  
* Spell checkers and dictionary implementations  
* IP routing (prefix matching)  
* Word games and pattern matching (e.g. Boggle, Scrabble AI)  

### Drawbacks

* Can use more memory than other data structures due to node overhead  
* Not well-suited for numeric or unordered key data  
* Slower than HashMaps for single-key lookups if words aren’t similar  
