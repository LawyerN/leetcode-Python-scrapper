from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        
        for num in nums:
            insertion_pos = bisect_left(arr, num)
            
            if insertion_pos == len(arr):
                arr.append(num)
            else:
                arr[insertion_pos] = num
        
        return len(arr)