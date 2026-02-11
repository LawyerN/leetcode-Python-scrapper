class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=[str(i) for i in digits]
        a=\'\'.join(a)
        a=str(int(a)+1)
        return [int(i) for i in a]