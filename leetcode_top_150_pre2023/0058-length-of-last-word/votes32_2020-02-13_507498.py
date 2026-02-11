# IDEA: scan from the end, increment the length counter if non-space found, otherwise keep skipping spaces
#       break and return the counter if space encountered AFTER we found any non-space
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenLast = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != \' \':
                lenLast += 1
            elif lenLast > 0:
                break
        return lenLast