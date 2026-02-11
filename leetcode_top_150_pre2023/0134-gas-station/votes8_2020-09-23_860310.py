class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g-c for g, c in zip(gas, cost)]       # get difference between gas & cost
        idx, min_val, cur = 0, sys.maxsize, 0         # get cumulative sum and find the smallest, the place after the smallest idx will be where we start
        for i, v in enumerate(diff):
            cur += v 
            if cur <= min_val: min_val, idx = cur, i  # maintain smallest & its index
        return (idx+1)%len(diff) if cur >= 0 else -1  # if total sum is less than 0, meaning no possible place to start