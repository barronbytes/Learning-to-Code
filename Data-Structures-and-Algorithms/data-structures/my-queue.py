from typing import List, Any, Optional


class Queue:
    def __init__(self, data: List[Any]):
        self.items: List[Any] = data


    def size(self) -> int:
        return len(self.items)


    def peek(self) -> Optional[Any]:
        return self.items[-1] if self.items else None


    def enqueue(self, item: Any) -> Any:
        self.items.insert(0, item)
        return item


    def dequeue(self) -> Optional[Any]:
        if not self.items:
            return None
        last_item = self.items[-1]
        del self.items[-1]
        return last_item


data = ["e", "d", "c", "b", "a"]
demo = Queue(data)


print(f"Data: {demo.items}")                                 # ['a', 'b', 'c', 'd', 'e']
print(f"Create: {demo.enqueue('Hello')} ... {demo.items}")   # Hello ... ['Hello', 'a', ..., 'e'] added to index 0!!!
print(f"Read (first item): {demo.peek()}")                   # Hello ... set to 'last' index!!!
print(f"Delete (FIFO): {demo.dequeue()} ... {demo.items}")   # Hello ... ['a', ..., 'e']
