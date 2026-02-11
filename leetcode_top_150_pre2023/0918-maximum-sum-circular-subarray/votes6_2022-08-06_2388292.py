class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp = [0] *len(nums)
        dp_min = [0] * len(nums)
        dp[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            dp_min[i] = min(dp_min[i-1]+nums[i],nums[i])
     
        if sum(nums) == min(dp_min):
            return max(dp)
        
        return max(max(dp),sum(nums)-min(dp_min))