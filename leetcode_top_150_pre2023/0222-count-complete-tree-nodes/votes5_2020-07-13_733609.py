class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def dfs(node):
            if not node: return 0

            left = node.left
            left_count = 1
            while left:
                left = left.left
                left_count += 1

            right = node.right
            right_count = 1
            while right:
                right = right.right
                right_count += 1

            if left_count == right_count:
                return (2**left_count) - 1
            else:
                left = dfs(node.left)
                right = dfs(node.right)

                return left + right + 1
        
        return dfs(root)