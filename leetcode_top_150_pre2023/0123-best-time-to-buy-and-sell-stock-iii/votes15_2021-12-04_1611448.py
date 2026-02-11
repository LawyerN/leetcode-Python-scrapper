class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, t, bought):
            if i >= len(prices) or t == 0:
                return 0
            
            # Skip
            profit = dp(i + 1, t, bought);

            # Sell
            if bought:
                profit = max(profit, dp(i + 1, t - 1, not bought) + prices[i])
            # Buy
            else:
                profit = max(profit, dp(i + 1, t, not bought) - prices[i])

            return profit
        
        return dp(0, 2, False)
        
\'\'\'
Approach: top-down recursive with memoization. On each day, we have three options: buy, sell, or skip (do nothing). In practice,
the recursion tree for this program will only have two branches because we can represent the choice to skip by not decrementing the number of transactions we can still make.
T: O(n), S: O(n)
\'\'\'