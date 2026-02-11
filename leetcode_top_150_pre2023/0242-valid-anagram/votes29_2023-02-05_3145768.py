class Solution:
    def allZeroes(self, count):
        for i in range(26):
            if count[i] != 0:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        count = [0] * 26
        for i in range(n):
            count[ord(s[i]) - ord(\'a\')] += 1
            count[ord(t[i]) - ord(\'a\')] -= 1
        if self.allZeroes(count) == False:
            return False
        return True