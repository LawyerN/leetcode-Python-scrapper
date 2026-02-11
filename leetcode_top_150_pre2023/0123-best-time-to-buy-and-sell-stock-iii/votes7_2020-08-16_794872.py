class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case of nothing to buy and sell
        if len(prices) < 2:
            return 0
        # edge case of only two days
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        one = -sys.maxsize-1
        two = 0
        three = -sys.maxsize-1
        four = 0
        i = 0
        while i < len(prices):
            one = max(one, -prices[i])
            two = two if i>=len(prices)-1 else max(two, one + prices[i+1])
            three = three if i>=len(prices)-2 else max(three, two - prices[i+2])
            four = four if i>=len(prices)-3 else max(four, three + prices[i+3])
            i+=1
        
        return max(two, four)