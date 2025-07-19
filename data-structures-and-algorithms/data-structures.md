# Data Structures

Learning data structures is *super* hard! Building them from scratch turned out to be a great way to learn. I coded some on my own and leaned on AI for others—I'm looking at you, [Red-Black Tree](https://github.com/barronbytes/learning-to-code/blob/main/data-structures-and-algorithms/data-structures/my_red_black_tree.py)! 😅 These guiding questions helped me think through each one:

1. What does it do?
2. What is it needed for?
3. What methods exist and what rules must be followed?
4. What edge cases should I consider?
5. What are the drawbacks to this data structure?
6. What is the best and worst case time complexity for methods?

## Stacks

### 1. Purpose

A stack is a **linear data structure** that stores elements using the **Last In, First Out (LIFO)** principle. This means the last item added is the first one removed. Think of it like a stack of plates—add to the top, remove from the top.

**Use Cases:** Stacks are useful for the following:
* Undo/redo functionality in text editors
* Managing browser history (back/forward)

### 2. Drawbacks

**O(1)** in best case with the folling considerations:
* Limited access: can only access last (newest) element
* No direct access to first (oldest) and middle elements
* Inefficient for searching or accessing non-top elements

## Queues

### 1. Purpose

A queue is a **linear data structure** that stores elements using the **First In, First Out (FIFO)** principle. This means the first item added is the first one removed—like people lining up in a queue at a store: first in, first out.

**Use Cases:** Queues are useful for the following:

* Task scheduling (e.g., print jobs, OS process management)
* Buffering data streams (e.g., I/O buffering, network packets)

### 2. Drawbacks

**O(1)** in best case with the folling considerations:
* Limited access: can only access the front and rear elements
* No direct access to middle elements
* Not ideal for scenarios requiring frequent random access or reverse-order processing

## Linked Lists

## Binary Trees

## Red-Black Trees