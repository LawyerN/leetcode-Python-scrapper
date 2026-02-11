class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        if nums[0] >= target:
            return 1

        minimum = float("inf")
        for i in range(len(nums)):
            subarray_sum = 0
            for j in range(i,len(nums)):
                subarray_sum += nums[j]
                if j - i < minimum and subarray_sum == target:
                    minimum = j - i + 1
                
        if minimum == float("inf"):
            return 0
        else:
            return minimum