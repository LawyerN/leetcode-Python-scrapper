class Solution(object):
    def findPeakElement(self, nums):
        nums.insert(0, float(\'-inf\'))
        nums.append(float(\'-inf\'))
        
        l, h = 1, len(nums) - 2
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid] > nums[mid-1]:
                l = mid + 1
            else:
                h = mid - 1