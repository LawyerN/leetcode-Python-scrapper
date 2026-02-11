class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## RC ##
        ## APPROACH ##
        ## Using division is sipmle ##
        # we can make use of the product of all the numbers to the left and all the numbers to the right of the index. Multiplying these two individual products would give us the desired result as well. ##
        # ==> left product [1,2,3,4] ==> [1,1,2,6] (left to right)
        # ==> right product [1,2,3,4] ==> [24,12,4,1] (right to left)
        # ==> multiplying these two will get answer.
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        size = len(nums)
        leftProduct = [0]*size
        rightProduct = [0]*size
        leftProduct[0] = 1
        rightProduct[size-1] = 1
        
        for i in range(1,size):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            rightProduct[size-i-1] = rightProduct[size-i] * nums[size-i]
        
        ans = []
        for i in range(size):
            ans.append(leftProduct[i] * rightProduct[i])
        return ans