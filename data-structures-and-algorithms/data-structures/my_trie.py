# This file completed with AI
from typing import Any, Dict, List


class Trie:
    """
    Trie class.

    Core Methods: __init__(), add(), exists(), words_with_prefix(), find_matches()
    Internal Helpers: _search_level() (used by words_with_prefix)

    Design Notes:
    - Trie is implemented as a nested dictionary structure
    - Each character of a word leads to a deeper level in the dictionary
    - An end_symbol "*" marks the end of a valid word
    """

    def __init__(self) -> None:
        # Initialize an empty root node and end-of-word symbol
        self.root: Dict[str, Any] = {}
        self.end_symbol: str = "*"


    def add(self, word: str) -> None:
        # Add a word to the trie by creating nested dictionary levels
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True


    def exists(self, word: str) -> bool:
        # Return True if the word exists in the trie; False otherwise
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return self.end_symbol in current


    def words_with_prefix(self, prefix: str) -> List[str]:
        # Return all words that start with prefix
        collected_words = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix, collected_words)


    def search_level(self, current_level: Dict[str, Any], current_prefix: str, words: List[str]) -> List[str]:
        # Helper for words_with_prefix: recursively collect words
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for letter in sorted(current_level.keys()):
            if letter != self.end_symbol:
                self.search_level(current_level[letter], current_prefix + letter, words)
        return words


    def find_matches(self, document: str) -> set:
        # Return a set of words found in the document that exist in the trie
        matches = set()
        for i in range(len(document)):
            current = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in current:
                    break
                current = current[ch]
                if self.end_symbol in current:
                    matches.add(document[i : j + 1])
        return matches


# --- Example Usage ---
trie = Trie()

# Add words
trie.add("cat")
trie.add("car")
trie.add("cart")
trie.add("dog")

# Check existence
print("Exists 'car'?: ", trie.exists("car"))                # True
print("Exists 'cab'?: ", trie.exists("cab"))                # False

# Words with prefix
print("Words with 'ca': ", trie.words_with_prefix("ca"))    # ['cat', 'car', 'cart']
print("Words with 'do': ", trie.words_with_prefix("do"))    # ['dog']
print("Words with 'z':  ", trie.words_with_prefix("z"))     # []

# Find matches in document
doc = "thecartandcatplayed"
print("Matches in doc: ", trie.find_matches(doc))           # {'cat', 'car', 'cart'}
