class Solution:
    def __init__(self):
        self.maxSum = float(\'-inf\')
    def maxPathSum(self, root: TreeNode) -> int:
        def traverse(root):
            if root:
                left = traverse(root.left)
                right = traverse(root.right)
                self.maxSum = max(self.maxSum,root.val, root.val + left, root.val + right, root.val + left + right)
                return max(root.val,root.val + left,root.val + right)
            else:
                return 0
        traverse(root)
        return self.maxSum