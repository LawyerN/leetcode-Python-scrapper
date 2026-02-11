from collections import OrderedDict, defaultdict

class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

    def addWord(self, word):
        if not word:
            self.isEnd = True
            return
        self.children[word[0]].addWord(word[1:])

class Solution:

    def findWords(self, board, words):
        self.root = TrieNode(); self.found = set(); self.R = len(board); self.C = len(board[0])
        
        for word in words:
            self.root.addWord(word)

        for r in range(self.R):
            for c in range(self.C):
                self.traverse(board, r, c, self.root, OrderedDict())
        return list(self.found)

    def traverse(self, board, r, c, trieNode, visited):
        
        if trieNode.isEnd:
            self.found.add(\'\'.join(visited.values()))

        if r < 0 or c < 0 or r >= self.R or c >= self.C or board[r][c] not in trieNode.children or (r,c) in visited:
            return
        
        visited[(r,c)] = board[r][c]
        self.traverse(board, r + 1, c, trieNode.children[board[r][c]], visited)
        self.traverse(board, r - 1, c, trieNode.children[board[r][c]], visited)
        self.traverse(board, r, c - 1, trieNode.children[board[r][c]], visited)
        self.traverse(board, r, c + 1, trieNode.children[board[r][c]], visited)
        del visited[(r,c)]