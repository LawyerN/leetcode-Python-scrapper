class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [0]*len(nums) # initialize left array 
        rightProducts = [0]*len(nums) # initialize right array
        
        leftProducts[0] = 1 # the left most is 1
        rightProducts[-1] = 1 # the right most is 1
        res = [] # output
        
        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1]*nums[i-1]
            rightProducts[len(nums) - i - 1] = rightProducts[len(nums) - i]*nums[len(nums) - i]
            
        for i in range(len(nums)):
            res.append(leftProducts[i]*rightProducts[i])
        
        return res