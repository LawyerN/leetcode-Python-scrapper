# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        ## dictionary
        # key: number
        # value: index in inorder array
        val_index_dict = { num:idx for idx, num in enumerate(inorder) }
        
        def helper( left, right):
            
            if left > right:
                # Base case:
                # return empty node as leaf node\'s child
                return None
            
            else:
                
                # Recall:
                # definition of postorder traversal: Left, Right, Center
                # rebuild with reversed direction ( from right to left )
                root = TreeNode( postorder.pop() )
                
                mid = val_index_dict[ root.val ]
                
                root.right = helper( mid+1, right)
                root.left = helper( left, mid-1 )
                return root
        # ----------------------------------------------------
        
        ## Top-down rebuild binary tree with definition
        return helper( left = 0, right = len(inorder)-1 )