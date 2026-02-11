class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0 # keep track of left pointer
        rsum = 0 # keep the running sum
        res = None # Answer we will return
        
        # Iterate through the array, the index will be your right pointer
        for right in range(len(nums)):
            
            # Add the current value to the running sum
            rsum += nums[right]
            
            # Once you reach a value at or equal to the target you
            # can use a while loop to start subtracting the values from left
            # to right so that you can produce the minimum size subarray
            while rsum >= target:
                
                # The result is either the current result you have, 
                # or the count of numbers from the current left position 
                # to the rightmost position. You need it to be right + 1 
                # because index starts at 0 (if you based the right as the 
                # last index it would be 4 or len(nums) - 1)
                
                # If res is None we compare it against the max float, 
                # saves us from having an if/else
                res = min(res or float(\'inf\'), right + 1 - left)
                
                # Subtract the number to see if we can continue subtracting based
                # on the while loop case and increment the left pointer
                rsum -= nums[left]
                left += 1

        return res or 0