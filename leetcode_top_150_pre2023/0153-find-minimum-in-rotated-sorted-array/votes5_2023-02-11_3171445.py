class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Keeping it simple, no fancy lamda\'s here for now
        min = 1e9
        for num in nums:
            if num < min:
                min = num

        return min