class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:        
        max_ans = float(\'-inf\')
        def helper(root):
            nonlocal max_ans
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            max_ans = max(max_ans,root.val,root.val+l,root.val+r,root.val+l+r)
            return max(root.val,root.val+l,root.val+r)
        helper(root)
        return max_ans