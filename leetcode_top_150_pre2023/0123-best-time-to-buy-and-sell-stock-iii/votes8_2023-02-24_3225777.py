class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float("inf")
        profit1 = profit2 = 0
        
        # Iterate through the prices and update the maximum profits
        for price in prices:
            # Update the price at which we should buy the first stock
            buy1 = min(buy1, price)
            # Update the profit we can make if we sell the first stock at this price
            profit1 = max(profit1, price - buy1)
            # Update the price at which we should buy the second stock
            buy2 = min(buy2, price - profit1)
            # Update the profit we can make if we sell the second stock at this price
            profit2 = max(profit2, price - buy2)
        
        # Return the maximum profit we can achieve after the second transaction
        return profit2