class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        nums.append(float(\'-inf\')) # index -1 and n will both get this in python
        while start <= end: # binary search to eliminate half each time
            mid = (start + end) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1