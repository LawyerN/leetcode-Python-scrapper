class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = [0] * 128
        for c in t:
            m[ord(c)] += 1
        start = 0
        end = 0
        counter = len(t)
        minStart = 0
        minLen = float(\'inf\')
        size = len(s)
        while end < size:
            if m[ord(s[end])] > 0:
                counter -= 1
            m[ord(s[end])] -= 1
            end += 1
            while counter == 0:
                if end - start < minLen:
                    minStart = start
                    minLen = end - start
                m[ord(s[start])] += 1
                if m[ord(s[start])] > 0:
                    counter