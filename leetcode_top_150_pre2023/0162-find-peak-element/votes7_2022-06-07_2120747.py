class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        l=1
        h=len(nums)-1
        while l<h:
            m=(l+h)//2
            if nums[m-1]<nums[m]>nums[m+1]:
                return m
            elif nums[m-1]<nums[m]<nums[m+1]:
                l=m+1
            else:
                h=m
            
        return l