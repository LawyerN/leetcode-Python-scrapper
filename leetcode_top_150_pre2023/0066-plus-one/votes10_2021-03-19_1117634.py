class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = \'\'.join(map(str, digits))
        b = int(a) + 1
        c = str(b)
        return list(map(int, c))