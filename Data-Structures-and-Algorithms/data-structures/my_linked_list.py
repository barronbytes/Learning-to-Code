from typing import Any, Optional
from linked_list_node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def add_to_head(self, value) -> None:
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    
    def add_to_tail(self, value) -> None:
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def remove_from_head(self) -> Optional[Any]:
        if not self.length:
            return None
        remove_node = self.head
        self.head = remove_node.next
        self.length -= 1
        if not self.head:
            self.tail = None
        return remove_node


ll = LinkedList()