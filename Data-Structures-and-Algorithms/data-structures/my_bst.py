from typing import List, Any


class BST:
    """
    Binary search tree class.
    
    Core Methods: insert(), search(), contains(), delete()
    Traversal Methods: inorder(), preorder(), postorder(), level_order()
    Utility / Helper Methods: get_min(), get_max(), height(), is_balanced(), size()
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def insert(self, value) -> None:
        if value == self.value:
            return
        elif value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)


    def inorder(self) -> List[Any]:
        values = []
        if self.left:
            values += self.left.inorder()
        values.append(self.value)
        if self.right:
            values += self.right.inorder()
        return values


    def get_min(self) -> Any:
        current = self
        while current.left:
            current = current.left
        return current.value


    def get_max(self) -> Any:
        current = self
        while current.right:
            current = current.right
        return current.value


    @staticmethod
    def set_root(values: List[Any]) -> "BST":
        if not values:
            raise ValueError("List of values must not be empty.")
        root = BST(values[0])
        for val in values[1:]:
            root.insert(val)
        return root


values = [20, 10, 25, 5, 15, 30, 12]
root = BST.set_root(values)
sorted_values = root.inorder()

print("Original data:", values)
print("Inorder Traversal:", sorted_values)
print("Minimum:", root.get_min())
print("Maximum:", root.get_max())
