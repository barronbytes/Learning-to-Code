from typing import List, Any, Optional


class Stack:
    def __init__(self, data: List[Any]):
        self.items: List[Any] = data


    def size(self) -> int:
        return len(self.items)


    def peek(self) -> Optional[Any]:
        return self.items[-1] if self.items else None


    def push(self, item: Any) -> Any:
        self.items.append(item)
        return item


    def pop(self) -> Optional[Any]:
        if not self.items:
            return None
        last_item = self.items[-1]
        del self.items[-1]
        return last_item


data = ["a", "b", "c", "d", "e"]
demo = Stack(data)


print(f"Data: {demo.items}")                                # ['a', 'b', 'c', 'd', 'e']
print(f"Create: {demo.push('Hello')} ... {demo.items}")     # Hello ... ['a', ..., 'e', 'Hello']
print(f"Read (last item): {demo.peek()}")                   # Hello
print(f"Delete (LIFO): {demo.pop()} ... {demo.items}")      # Hello ... ['a', ..., 'e']
