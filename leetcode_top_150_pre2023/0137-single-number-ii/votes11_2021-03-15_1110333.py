class Solution(object):
    def singleNumber(self, nums):
        a, b = 0, 0
        for x in nums:
            a, b = (~x&a&~b)|(x&~a&b), ~a&(x^b)
        return b