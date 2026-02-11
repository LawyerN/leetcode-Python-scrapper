## Approach 2:
Similar to problem 0045 Jump Game II, but here we need to check if we can reach the end. As in problem 0045 we can create cumulative maximum of i + nums[i] and check if for some element we have i == t[i]: if we have such place, we stuck and we can not reach the last cell, if not, we can reach.

### Code: