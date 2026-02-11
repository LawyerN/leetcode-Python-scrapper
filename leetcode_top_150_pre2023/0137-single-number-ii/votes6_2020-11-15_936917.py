class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for c in nums:
            b = (b ^ c) & ~a
            a = (a ^ c) & ~b
        return b