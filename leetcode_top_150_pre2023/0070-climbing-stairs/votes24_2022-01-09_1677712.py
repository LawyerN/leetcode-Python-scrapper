class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(i):
            if i==0:
                return 1
            if i<0:
                return 0
        
            wayone=stairs(i-1)
            waytwo=stairs(i-2)
            
            return wayone+waytwo
        
    
        return stairs(n)