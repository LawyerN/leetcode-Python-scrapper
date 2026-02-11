class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        
        @lru_cache(maxsize=None)
        def solve(t_left: int, i:int, bought_price: int):
            if i == n or t_left == 0:
                return 0
            
            # Not holding a stock
            if bought_price == -1:
                buy = 0
                # buy (optimize for minima)
                if not (i+1 < n and prices[i+1] < prices[i]):
                    buy = solve(t_left, i+1, prices[i])
                # or not buy
                not_buy = solve(t_left, i + 1, -1)
                return max(buy, not_buy)
        
            # holding
            else:
                sell = 0
                # make profit optimization + maxima optimization
                if prices[i] - bought_price > 0 and not (i+1 < n and prices[i+1] > prices[i]):
                    sell = prices[i] - bought_price + solve(t_left - 1, i + 1, -1)
                
                # if you don\'t sell, optimize minima
                not_sell = solve(t_left, i + 1, min(bought_price, prices[i]))
                return max(sell, not_sell)
        
        return solve(k, 0, -1)