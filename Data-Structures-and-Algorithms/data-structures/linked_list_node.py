class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def __repr__(self) -> str:
        next_value = self.next.value if self.next else None
        return f"Node(value={self.value}, next={next_value})"


    def set_next(self, node: "Node") -> None:
        self.next = node