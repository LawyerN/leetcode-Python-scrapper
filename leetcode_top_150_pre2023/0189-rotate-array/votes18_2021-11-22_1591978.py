def rotate(self, nums, k):
        k = k % len(nums)                 #take care of the case where k >= len(nums)  
        nums[:] = nums[-k:] + nums[:-k]