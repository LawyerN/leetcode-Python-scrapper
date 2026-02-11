class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr = 0
        max_sum = float(\'-inf\')
        flag = 1
        ans = float(\'-inf\')
        # check if all elements are negative
        for i in nums:
            if i >= 0:
                flag = 0
                break
            ans = max(ans, i)
        # if all elements are negative return the largest one
        if flag:
            return ans
        # find max subarray sum using kadane\'s algorithm
        for i in nums:
            total_sum += i
            curr += i
            max_sum = max(max_sum, curr)
            if curr < 0:
                curr = 0
        min_sum = float(\'inf\')
        curr = 0
        # find min subarray sum
        for i in nums:
            curr += i
            min_sum = min(min_sum, curr)
            if curr > 0:
                curr = 0
        # find the maximum sum of subarray by comparing the max subarray sum and total sum - min subarray sum
        ans2 = total_sum - min_sum
        return max(max_sum, ans2)