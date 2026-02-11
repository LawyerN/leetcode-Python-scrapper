# A fast trie implementation, not as readable as using TrieNodes but
# more performant.
#
# https://github.com/raul-sauco/coding-challenges/blob/main/leetcode/implement-trie-prefix-tree.py
#
class Trie:
    def __init__(self, words: List[str] = None):
		# The variable length stores the total number of children of this node.
        self.root = {"length": 0}
        for word in words:
            self.insert(word)
			
	# Having a len method helps debug.
    def __len__(self) -> int:
        return self.root["length"]

    # Insert a word into this trie object. O(1) because max word length is 10 chars.
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {"length": 0}
            # There is more complete word under this node.
            current["length"] += 1
            current = current[c]
        current["length"] += 1
        current["?"] = True

    # Remove a word from this trie object. O(1) because max word length is 10.
    def remove(self, word: str) -> None:
        current = self.root
        current["length"] -= 1
        for i, c in enumerate(word):
            if c in current:
                current[c]["length"] -= 1
                if current[c]["length"] < 1:
                    current.pop(c)
                    break
                else:
                    current = current[c]
        # If we get to the word leaf but the trie node has children.
        if i == len(word) - 1 and "?" in current:
            current.pop("?")

    # Check if a given list of chars is in the trie, it returns 0 if
    # not found, 1 if found but not a full word and 2 if a full word.
	# O(1) because max word length is 10.
    def contains(self, word: List[str]) -> int:
        current = self.root
        for c in word:
            if c not in current:
                return 0
            current = current[c]
        return 2 if "?" in current else 1