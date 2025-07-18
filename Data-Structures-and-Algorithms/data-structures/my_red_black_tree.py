# This file completed with AI
from typing import Optional, Any
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLACK = auto()


class RBNode:
    """
    Red-Black Tree class.

    Core Methods: insert()
    Internal Fixing: _insert_fixup(), _rotate_left(), _rotate_right()
    Sentinel: Uses a self-referential NIL node to simplify edge cases

    Maintains balanced height with O(log n) insertions by enforcing rules:
    1. Every node is either red or black
    2. Root node always black
    3. All NIL leaf nodes are black
    4. If a node is red, then both its children are black
    5. Every path from a node to its descendant NILs has the same number of black nodes
    """
    def __init__(
        self,
        value: Optional[Any],
        color: Color = Color.RED,
        parent: Optional["RBNode"] = None,
        left: Optional["RBNode"] = None,
        right: Optional["RBNode"] = None
    ) -> None:
        # Initialize a red-black tree node with value, color, and optional parent/children
        self.value: Optional[Any] = value
        self.color: Color = color
        self.parent: Optional["RBNode"] = parent
        self.left: Optional["RBNode"] = left
        self.right: Optional["RBNode"] = right


class RBTree:
    def __init__(self) -> None:
        # Initialize an empty red-black tree with a self-referential sentinel NIL leaf node to avoid None checks
        # Must keep self.NIL unchanged throughout tree for reuse by all new nodes!!!
        self.NIL: RBNode = RBNode(value=None, color=Color.BLACK)
        self.NIL.parent = self.NIL
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root: RBNode = self.NIL


    def insert(self, value: Any) -> None:
        # Create new node with self.NIL children and parent set to None for now
        new_node = RBNode(
            value=value,
            color=Color.RED,
            left=self.NIL,
            right=self.NIL,
            parent=None
        )

        parent = self.NIL
        current = self.root

        # Initialize traversal from the root to find the correct insertion point
        # `current` moves through the tree; `parent` lags one level behind to track where to attach the new node
        while current != self.NIL:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return  # Duplicate values not allowed

        # Set the new node's parent
        new_node.parent = parent

        if parent == self.NIL:
            # Tree was empty
            self.root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix any Red-Black violations
        self._insert_fixup(new_node)


    def _insert_fixup(self, node: RBNode) -> None:
        """
        Restore red-black properties after insertion
        Fix cases where red parent causes violation by rotating and recoloring
        """
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == Color.RED:
                    # Case 1: Uncle is red → Recolor parent, uncle, grandparent
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child → Left rotate parent
                        node = node.parent
                        self._rotate_left(node)
                    # Case 3: Node is left child → Right rotate grandparent
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rotate_right(node.parent.parent)
            else:
                # Mirror case (node is in right subtree)
                uncle = node.parent.parent.left

                if uncle.color == Color.RED:
                    # Case 1 (mirror): Recolor
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2 (mirror): Right rotate parent
                        node = node.parent
                        self._rotate_right(node)
                    # Case 3 (mirror): Left rotate grandparent
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rotate_left(node.parent.parent)

        self.root.color = Color.BLACK


    def _rotate_left(self, x: RBNode) -> None:
        """
        Perform a left rotation around the given node x.
        
        This makes x.right the new root of the subtree,
        and x becomes the left child of its previous right child.
        """
        y = x.right  # y will become the new root of the subtree
        x.right = y.left  # move y's left subtree to x's right
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent  # link y's parent to x's parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x  # put x on y's left
        x.parent = y


    def _rotate_right(self, y: RBNode) -> None:
        """
        Perform a right rotation around the given node y.
        
        This makes y.left the new root of the subtree,
        and y becomes the right child of its previous left child.
        """
        x = y.left  # x will become the new root of the subtree
        y.left = x.right  # move x's right subtree to y's left
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent  # link x's parent to y's parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y  # put y on x's right
        y.parent = x


# --- Example Usage ---
tree = RBTree()
values = [20, 10, 25, 5, 15, 30]
for v in values:
    tree.insert(v)

print("Root:", tree.root.value, "| Color:", tree.root.color)
print("Root Left:", tree.root.left.value, "| Color:", tree.root.left.color)
print("Root Right:", tree.root.right.value, "| Color:", tree.root.right.color)
print("Left Child of Root Left:", tree.root.left.left.value, "| Color:", tree.root.left.left.color)
