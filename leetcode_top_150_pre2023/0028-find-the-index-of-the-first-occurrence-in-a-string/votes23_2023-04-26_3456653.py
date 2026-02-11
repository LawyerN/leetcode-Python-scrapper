class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        i = 0
        j = len(needle)
        while j <= len(haystack):
            currentNeedle = haystack[i:j]
            if currentNeedle == needle:
                return i
            i += 1
            j += 1
        return -1