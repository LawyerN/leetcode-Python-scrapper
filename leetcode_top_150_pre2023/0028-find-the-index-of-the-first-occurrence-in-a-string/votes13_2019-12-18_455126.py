class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        stride = len(needle)
        haystack_length = len(haystack)
        total_step = haystack_length-stride+1
        if stride == 0: return 0
        for i in range(total_step):
            if haystack[i:i+stride] == needle:
                return i
        return -1