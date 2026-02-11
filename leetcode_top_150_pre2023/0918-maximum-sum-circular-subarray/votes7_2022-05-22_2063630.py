def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        if len(nums) ==1:
            return nums[0]
        
        """kadane algorithm for maximum sum subarray """
       
        def kadane(nums):
            ans = nums[0]
            sum_so_far = 0
            for x in nums:
                
                sum_so_far += x
                if sum_so_far > ans:
                    ans = sum_so_far
                
                if sum_so_far<0:
                    sum_so_far = 0
                    
            return ans 
		#maximum subarray sum when there is no wrapping involved 
        max_subarray_sum_1 = kadane(nums)
		# if wrapping is involved then the idea is calculate min subarray sum and subtract it with total sum. 
        max_subarray_sum_2 = -sum([-1*x for x in nums]) + kadane([-1*x for x in nums])
        
        res = max(max_subarray_sum_1, max_subarray_sum_2)
        # print(res, max_subarray_sum_1)
		# what if all elements of the array are negative i.e. [-1,-2,-2] in this case sum=-5 + min_subarray_sum(-5) wich will give 0 
		# in this case we can return maximum subarray sum which is our answer 
        return res if res!=0 else max_subarray_sum_1