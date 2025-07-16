from typing import Any, Optional, Iterator
from linked_list_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            # Use the Node's __repr__ or just its value
            nodes.append(repr(current.value))  # or str(current.value)
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty LinkedList"


    def add_to_head(self, value: Any) -> None:
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    
    def add_to_tail(self, value: Any) -> None:
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def remove_from_head(self) -> Optional[Node]:
        if not self.length:
            return None
        remove_node = self.head
        self.head = remove_node.next
        self.length -= 1
        if not self.head:
            self.tail = None
        return remove_node


ll = LinkedList()

# Initial state
print(f"Initial list: {ll}")            # Empty LinkedList

# Add elements to tail
ll.add_to_tail("a")
ll.add_to_tail("b")
ll.add_to_tail("c")
print(f"After adding to tail: {ll}")    # 'a -> b -> c'

# Add elements to head
ll.add_to_head("z")
ll.add_to_head("y")
print(f"After adding to head: {ll}")    # 'y -> z -> a -> b -> c'

# Remove head
removed = ll.remove_from_head()
print(f"Removed from head: {removed}")  # Node(value=y, next=z)
print(f"List after removal: {ll}")      # 'z -> a -> b -> c'

# Iterate over values
print("Iterating over list:")
for value in ll:
    print(f"  value: {value}")          # z, a, b, c

# Check current head and tail values
print(f"Head: {ll.head.value}")         # z
print(f"Tail: {ll.tail.value}")         # c

# Final state
print(f"Final list: {ll}")              # 'z -> a -> b -> c'
print(f"Length: {ll.length}")           # 4
