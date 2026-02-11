class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        HOLD_STOCK, KEEP_CASH = 0, 1
        
        # dictionary
        # key: state, kth-transaction
        # value: corresponding profit
        dp = defaultdict(int)        
        
        # No free lunch, impoosible to have stock before first trading day
        dp[(HOLD_STOCK, 0)] = -math.inf
        dp[(HOLD_STOCK, 1)] = -math.inf
        dp[(HOLD_STOCK, 2)] = -math.inf
        

        for stock_price in prices:

            ## For 1st transaction:
            # Either we kept cash already, or we just sell out stock today
            dp[KEEP_CASH, 1] = max(dp[KEEP_CASH, 1], dp[HOLD_STOCK, 1] + stock_price )
            
            # Either we had stock already, or we just buy in stock today ( add one more transaction)
            dp[HOLD_STOCK, 1] = max(dp[HOLD_STOCK, 1],  dp[KEEP_CASH, 0] - stock_price)
            
            ## For 2nd transaction:
            # Either we kept cash already, or we just sell out stock today
            dp[KEEP_CASH, 2] = max(dp[KEEP_CASH, 2], dp[ HOLD_STOCK, 2] + stock_price)

            # Either we had stock already, or we just buy in stock today ( add one more transaction)
            dp[HOLD_STOCK, 2] = max(dp[HOLD_STOCK, 2], dp[KEEP_CASH, 1] - stock_price)
            
        # Maximal profit must be KEEP_CASH on last day
        # (This means we cash out and sell stocks finally)
        return dp[KEEP_CASH, 2]