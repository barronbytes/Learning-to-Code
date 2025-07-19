# This file completed with AI
from typing import Any, Optional


class HashMap:
    """
    HashMap class.

    Core Methods: __init__(), insert(), get()
    Internal Helpers: _resize(), __repr__()
    
    Collision Resolution: Uses linear probing to handle key collisions
    Resize Strategy: Doubles in size when load factor exceeds 0.7

    Design Notes:
    - Only string keys are supported (can be extended)
    - Index is derived from the ASCII sum of characters in the key
    - Keys must be unique (no support for duplicate keys)
    """
    def __init__(self, initial_size: int = 8) -> None:
        # Initialize the hashmap with a fixed-size empty list and counters
        self.size = initial_size
        self.filled_count = 0
        self.data = [None] * self.size


    def __repr__(self) -> str:
        # Return a string representation of the stored key-value pairs
        return str([pair for pair in self.data if pair is not None])


    def insert(self, key: str, value: Any) -> None:
        # Insert or update a key-value pair, resizing if load factor is too high
        if not isinstance(key, str):
            raise TypeError("Keys must be strings.")

        if self.filled_count / self.size > 0.7:
            self._resize()

        index = sum(ord(char) for char in key) % self.size

        # Use linear probing to find an available slot:
        # - If the current index is occupied by the same key, update the value and stop
        # - If occupied by a different key, move to the next index (wrapping around the array)
        # - Because we resize the hashmap before it gets too full (load factor > 0.7),
        #   we guarantee there will be an empty slot, preventing infinite loops
        while self.data[index] is not None:
            k, _ = self.data[index]
            if k == key:
                self.data[index] = (key, value)
                return
            index = (index + 1) % self.size

        self.data[index] = (key, value)
        self.filled_count += 1


    def get(self, key: str) -> Optional[Any]:
        # Retrieve the value associated with the given key or None if not found
        if not isinstance(key, str):
            raise TypeError("Keys must be strings.")

        index = sum(ord(char) for char in key) % self.size

        # Search forward from hash index only, since keys are inserted starting there; no need to check earlier slots
        while self.data[index] is not None:
            k, v = self.data[index]
            if k == key:
                return v
            index = (index + 1) % self.size

        return None


    def _resize(self) -> None:
        # Double the internal storage size and rehash all existing key-value pairs
        old_data = self.data
        self.size *= 2
        self.data = [None] * self.size
        self.filled_count = 0

        for pair in old_data:
            if pair is not None:
                key, value = pair
                self.insert(key, value)


# --- Example Usage ---
hm = HashMap()

# Insert key-value pairs
hm.insert("apple", 1)
hm.insert("banana", 2)
hm.insert("cherry", 3)
print("Full HashMap: ", hm)

# Retrieve values
print("Get `banana`?: ", hm.get("banana"))     # Output: 2
print("Get `grape`?:  ", hm.get("grape"))      # Output: None (not found)

# Overwrite value
hm.insert("banana", 42)
print("Get `banana`?: ", hm.get("banana"))     # Output: 42

# Print internal state
print("Full HashMap: ", hm)
