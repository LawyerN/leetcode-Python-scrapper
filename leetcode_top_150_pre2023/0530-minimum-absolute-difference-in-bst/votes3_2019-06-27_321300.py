class Solution:

    a, b = float("-inf"), float("inf")
	
    def getMinimumDifference(self, r: TreeNode) -> int:
        if not r: return r
        self.getMinimumDifference(r.left)
        self.b, self.a = min(self.b, r.val-self.a), r.val
        self.getMinimumDifference(r.right)
        return self.b