from typing import Optional, Any
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLACK = auto()


class RBNode:
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
