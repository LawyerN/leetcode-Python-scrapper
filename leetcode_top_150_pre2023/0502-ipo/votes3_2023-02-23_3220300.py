class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # sort the profits based on the capital required
        cap_profits = list(zip(capital, profits))
        cap_profits.sort()
        
        profit_list, proj_cnt, prev_proj_cnt = [], 0, -1
        
        idx = 0
        while proj_cnt < k and proj_cnt != prev_proj_cnt:
            prev_proj_cnt = proj_cnt
            while idx < len(profits) and cap_profits[idx][0] <= w:
                heapq.heappush(profit_list, -(cap_profits[idx][1]))
                idx += 1

            # pick the largest profit we can get from the profit list
            if profit_list:
                w -= heapq.heappop(profit_list)
                proj_cnt += 1
            
        return w