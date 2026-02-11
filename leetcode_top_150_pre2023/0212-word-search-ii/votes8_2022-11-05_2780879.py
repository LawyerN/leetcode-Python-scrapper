class TrieNode:
    def __init__(self):
        self.childs = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        ### construct trie
        self.trie_root = TrieNode()
        for word in words:
            cur = self.trie_root
            for char in word:
                if char not in cur.childs:
                    cur.childs[char] = TrieNode()
                cur = cur.childs[char]
            cur.end = True


        ### dfs branching algo
        def dfs(r, c, node, path):
            nonlocal m, n, out
            if node.end:
                out.add(path)
                if len(node.childs) == 0:
                    return True  # i.e. we have completed the whole branch (word end at leaf)
            
            if len(node.childs) > 0:
                for rr, cc in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                    if rr >= 0 and rr < m and cc >= 0 and cc < n:
                        letter = board[rr][cc]
                        if (rr, cc) not in seen and letter in node.childs:
                            seen.add((rr, cc))
                            done = dfs(rr, cc, node.childs[letter], path+letter)
                            if done:  # if the branch is completed, throw it away !
                                node.childs.pop(letter)
                            seen.remove((rr, cc))  # backtrack
            
            return len(node.childs)==0  # keep the branch only if not empty (this will backprop to top nodes)
            # by structure, a leaf node can only be either a word end, or a branch we started popping already.


        ### main
        out = set()  # use set to avoid duplicates
        for r in range(m):
            for c in range(n):
                letter = board[r][c]
                if letter in self.trie_root.childs:
                    seen = set([(r, c)])
                    dfs(r, c, self.trie_root.childs[letter], letter)

        return list(out)