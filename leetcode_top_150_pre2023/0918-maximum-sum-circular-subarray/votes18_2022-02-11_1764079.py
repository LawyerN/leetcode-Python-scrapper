class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # Assume the array is not circular and calculate max sub array sum.
        currentSum = nums[0]
        maxSum = nums[0]
        for i in range(1, n):
            currentSum = max(nums[i], nums[i]+currentSum)
            maxSum = max(currentSum, maxSum)
        
        # Assume the array is not circular and calculate min sub array sum.
        currentSum = nums[0]
        minSum = nums[0]
        for i in range(1, n):
            currentSum = min(nums[i], nums[i]+currentSum)
            minSum = min(currentSum, minSum)
        
        # Max sub array sum of a cirular array = max(maxSum, totalSum-minSum)
        """
            The above statement can be justified for circular array by understanding the following:
            1. If all the elements are positive then max sub array sum would be total sum.
            2. Now if there are few negative elements present then the total sum would be decreased by minimum sub array sum.
            3. Now to get the max sub array sum, we need to negate the factor(minimum sub array sum) that caused the decrement of total sum.
        """
        circularMaxSum = sum(nums)-minSum
        if circularMaxSum == 0:
            return maxSum
        return max(maxSum, circularMaxSum)