class Solution:
    def maximumHeight(self, root: TreeNode, height: int, ans: List[int]) -> None:
        if (root == None):
            return
        if(root.left == None and root.right == None):
            ans[0] = max(ans[0], height)
        self.maximumHeight(root.left, height+1, ans)
        self.maximumHeight(root.right, height+1, ans)

    def maxDepth(self, root: TreeNode) -> int:
        ans = [0]
        self.maximumHeight(root, 1, ans)
        return ans[0]