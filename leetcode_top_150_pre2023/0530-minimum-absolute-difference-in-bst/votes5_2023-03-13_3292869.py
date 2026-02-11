class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # initialize minimum difference and previous node value
        min_diff = float(\'inf\')
        prev_val = None
        
        # define a helper function for inorder traversal
        def inorder(node):
            nonlocal prev_val, min_diff
            
            if node is None:
                return
            
            # traverse left subtree
            inorder(node.left)
            
            # update minimum difference
            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)
            
            # update previous value
            prev_val = node.val
            
            # traverse right subtree
            inorder(node.right)
        
        # call inorder traversal on root and return minimum difference
        inorder(root)
        return min_diff