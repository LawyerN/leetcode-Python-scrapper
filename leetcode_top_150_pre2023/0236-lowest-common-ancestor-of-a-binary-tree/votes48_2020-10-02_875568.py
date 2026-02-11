# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        
        LCA in a binary tree..
        Think of it like a single node, we need to find the p and q
        our search will be over when we find p in our right and q in our left
        or vice versa, at that point, the root is the answer!
        
        """
        # I have reached a dead end, I didn\'t find anything here
        if not root:
            return None
        
        # I see one of the targets! I will inform my caller!
        if root == q or root == p: return root
        
        # Look in the left, if you find p or q , return yourself
        foundInLeft = self.lowestCommonAncestor(root.left, p, q)
        
        # Look in the right, if you find p or q , return yourself
        foundInRight = self.lowestCommonAncestor(root.right, p, q)
        
        # Didnt find anything in the left, must be in right
        if not foundInLeft: return foundInRight
        
        # Didnt find anything in the right, must be in the left
        if not foundInRight: return foundInLeft
        
        # Found something in both! Hence this is the one!
        return root