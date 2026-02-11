class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        to_visit = [(0, 0)]
        visited = set()
        dist = 0
        while to_visit:
            nxt_lvl = []
            while to_visit:
                i, j = to_visit.pop()
                if (i, j) in visited:
                    continue
                while i < n and j < m and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i == n and j == m:
                    return dist
                if (i, j + 1) not in visited:
                    nxt_lvl.append((i, j + 1))
                if (i + 1, j) not in visited:
                    nxt_lvl.append((i + 1, j))
                if (i + 1, j + 1) not in visited:
                    nxt_lvl.append((i + 1, j + 1))
                visited.add((i, j))
            dist += 1
            to_visit = nxt_lvl