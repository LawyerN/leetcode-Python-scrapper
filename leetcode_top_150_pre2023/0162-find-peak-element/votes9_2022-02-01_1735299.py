class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            # if we access out of bounds, set to negative infinity
            leftVal = nums[m - 1] if m - 1 >= 0 else float("-inf")
            rightVal = nums[m + 1] if m + 1 < len(nums) else float("-inf")
            
            # if nums[m] is a local maxima, return m (index)
            if nums[m] > leftVal and nums[m] > rightVal:
                return m
            
            # if nums is increasing from m to m + 1
            # search in that direction
            if nums[m] < nums[m + 1]:
                l = m + 1
            # otherwise, there is two cases. One is that
            # this is a local minima and both other sides are
            # higher, in which case it doesn\'t matter which way we search because either
            # will have a solution. Otherwise, nums[m - 1] is greater than nums[m] but nums[m + 1]
            # is not, in which case the lefthand side will again have a valid result
            else:
                r = m - 1