class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def get_tree_height( node: TreeNode) -> int:
            
            if not node:
                # base case
                return 0
            
            else:
                # general case
                return 1 + get_tree_height( node.left )
            
        # -----------------------------------------------
        
        def counting( node: TreeNode ) -> int:
            
            h = get_tree_height( node )
            
            if h == 0:
                # base case (with empty tree)
                return 0
            
            else:
                # general case
                if (h - 1) == get_tree_height( node.right ):
                    
                    # left subtree and right subtree are of the same height
                    # last node is on the right subtree
                    return 2 ** (h - 1) + counting( node.right )
                
                else:
                    # left subtree is higher than right subtree
                    # last node is on the left subtree
                    return 2 ** (h - 2) + counting( node.left )
        
        # -----------------------------------------------
        return counting(root)