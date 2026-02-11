class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Use a list to store the path from root to the current node
        stack = [(root, root.val)]
        
        while stack:
            node, val = stack.pop()
            
            # Check if the current node is a leaf node and its value matches the targetSum
            if not node.left and not node.right and val == targetSum:
                return True
            
            # Add the left and right children to the stack along with their updated path value
            if node.left:
                stack.append((node.left, val + node.left.val))
            if node.right:
                stack.append((node.right, val + node.right.val))
        
        return False