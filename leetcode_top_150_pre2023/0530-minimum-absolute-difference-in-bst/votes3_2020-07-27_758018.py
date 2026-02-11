class Solution:
    Inf = float(\'inf\')
    def getMinimumDifference(self, root): # -> int:
        self.best = Inf = self.Inf
        def dfs(n,a,b):
            if n:
                x = n.val
                self.best = min( self.best, x-a, b-x )
                dfs(n.left ,a,x)
                dfs(n.right,x,b)
        dfs(root,-Inf,Inf)
        return self.best