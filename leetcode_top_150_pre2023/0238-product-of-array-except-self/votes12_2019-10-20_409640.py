def productExceptSelf(self, nums: List[int]) -> List[int]:
		#output array (just fill empty with 1s)
        res = [1] * len(nums)
        #left and right pointers
        lo = 0
        hi = len(nums) - 1
        #product for left and right
        leftProduct = 1
        rightProduct = 1
        #keep going until pointers meet
        while lo < len(nums):
            #add running from the l/r products to these spots
            res[lo] *= leftProduct
            res[hi] *= rightProduct
            #multiply products by current in nums
            rightProduct *= nums[hi]
            leftProduct *= nums[lo]
            #inc/dec pointers
            lo += 1
            hi -= 1
        return res