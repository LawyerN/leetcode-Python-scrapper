# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff = sys.maxsize
        values = []
        def inorder(node, values=values):
            if node:
                inorder(node.left)
                if values:
                    self.min_diff = min(self.min_diff, abs(node.val - values[-1]))
                    
                values.append(node.val)
                inorder(node.right)
                
        inorder(root)
        return self.min_diff