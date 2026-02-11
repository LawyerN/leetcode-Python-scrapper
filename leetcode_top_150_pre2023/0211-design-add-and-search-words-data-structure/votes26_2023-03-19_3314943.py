class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWordCompleted = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord(\'a\')
            if newRoot.children[alphabetIndex] is None:
                newRoot.children[alphabetIndex] = TrieNode()
            newRoot = newRoot.children[alphabetIndex]
        newRoot.isWordCompleted = True
    
    def searchHelper(self, word: str, index: int, newRoot: TrieNode) -> bool:
        if index == len(word):
            return newRoot.isWordCompleted
        ch = word[index]
        if ch == \'.\':
            for i in range(26):
                if newRoot.children[i] is not None and self.searchHelper(word, index + 1, newRoot.children[i]):
                    return True
            return False
        else:
            alphabetIndex = ord(ch) - ord(\'a\')
            if newRoot.children[alphabetIndex] is None:
                return False
            return self.searchHelper(word, index + 1, newRoot.children[alphabetIndex])

    def search(self, word: str) -> bool:
        return self.searchHelper(word, 0, self.root)