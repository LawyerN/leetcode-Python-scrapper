class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for idx, val in enumerate(nums):
                if target - val in nums[idx + 1:]:
                    return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]