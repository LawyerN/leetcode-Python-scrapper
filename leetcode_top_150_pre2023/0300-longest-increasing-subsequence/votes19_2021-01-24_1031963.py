class Solution:
    # Dynamic Programming with Binary Search
    # Time complexity : O(nlogn). Binary search takes nlogn time and it is called n times.
    # Space complexity : O(n). dp array of size n is used.
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp keeps some of the visited element in a sorted list, and its size is lengthOfLIS sofar.
        # It always keeps the our best chance to build a LIS in the future.
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp):
                # If num is the biggest, we should add it into the end of dp.
                dp.append(num)
            else:
                # If num is not the biggest, we should keep it in dp and replace the previous num
                # in this position. Because even if num can\'t build longer LIS directly, it can
                # help build a smaller dp, and we will have the best chance to build a LIS in the
                # future. All elements before this position will be the best(smallest) LIS sor far. 
                dp[i] = num
        return len(dp)