class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : HASHMAP ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
        
        counter = collections.Counter(nums)
        for num in counter.keys():
            if counter[num] == 1:
                return num
        
        ## APPROACH : BIT MANIPULATION ##
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        # XOR operator which could be used to detect the bit which appears odd number of times: 1, 3, 5, etc.
        seen_once = seen_twice = 0
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don\'t add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don\'t add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num) # change seen_once only if seen_twice is unchanged
            seen_twice = ~seen_once & (seen_twice ^ num) # change seen_twice only if seen_once is unchanged
        return seen_once