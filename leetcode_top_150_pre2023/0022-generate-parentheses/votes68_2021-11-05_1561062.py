if left>0:
                helper(ans, s+\'(\', left-1, right)
                
            if right>0:
                helper(ans, s+\')\', left, right-1)