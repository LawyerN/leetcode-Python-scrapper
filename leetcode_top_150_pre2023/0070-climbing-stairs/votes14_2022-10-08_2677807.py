def climbStairs(self, n):
	if n <= 2: # there is 1 way to climb up 1 step and 2 ways to climb up 2 steps
		return n
	return self.climbStairs(n-1)+self.climbStairs(n-2) # we can get to this step from either of the last two steps