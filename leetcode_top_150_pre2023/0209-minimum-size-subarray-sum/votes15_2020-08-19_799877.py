class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        window_start = 0
        min_size = float(\'inf\')
		
		# summation of subarray
        summation = 0
        
        # use sliding window to update min_size of of valid subarray
        for window_end, number in enumerate(nums):
            
            summation += number
            
            while summation >= s:
                
                # keep shrinking window size if summation is valid
                min_size = min( min_size, window_end - window_start + 1)
                
                # update subarray sum
                summation -= nums[window_start]
                
                window_start += 1
                
        
        if min_size == float(\'inf\'):
            
            # no solution
            return 0
        
        else:
            
            return min_size