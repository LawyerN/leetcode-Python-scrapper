class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # the idea is to store previously seen numbers with
        # their corresponding indices in a hashmap/dict
        seen = dict()
        
        for i, n in enumerate(nums):
            if target-n in seen:
                return [i,seen[target-n]]
            else:
                seen[n] = i
                
        # this place is unreachable
        return [0,0]