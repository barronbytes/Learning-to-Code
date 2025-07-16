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