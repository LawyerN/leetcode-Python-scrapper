class Solution:
    def trap(self, h: List[int]) -> int:
        return sum(min(max(h[:i+1]),max(h[i:]))-v for i,v in enumerate(h))