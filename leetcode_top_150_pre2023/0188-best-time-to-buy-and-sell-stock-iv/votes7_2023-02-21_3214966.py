class Solution:
  def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    # edge case where there are no prices or no transactions
    if n == 0 or k == 0:
        return 0
    # edge case where we can perform an unlimited number of transactions
    if k >= n // 2:
        return sum(max(0, prices[i+1] - prices[i]) for i in range(n-1))
    # initialize dp table
    dp = [[0] * (k+1) for _ in range(n)]
    for j in range(1, k+1):
        max_diff = -prices[0] # keep track of the maximum difference seen so far
        for i in range(1, n):
            dp[i][j] = max(dp[i-1][j], prices[i] + max_diff)
            max_diff = max(max_diff, dp[i-1][j-1] - prices[i])
    return dp[n-1][k]