"""
             1 visit 
           /    \\ 
    (^3)  2      3 visit
        /   \\   /  
       4     5 6 visit
     
     visit half nodes so logn

"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.getLeftHeight(root) #logn op
        right = self.getRightHeight(root) #logn op
        
        if left == right:
            count = (2**left)-1 #if left == right then it\'s a complete BT. number of nodes in a comp BT is 2^h-1
            return count
        else:
            #one subtree will always return immediately because it is complete. Hence time complexity is O(logn)
            return self.countNodes(root.left) + self.countNodes(root.right) + 1 
        
    
    def getLeftHeight(self, root):
        count=1
        while root.left:
            count += 1
            root = root.left
        return count
    
    def getRightHeight(self, root):
        count=1
        while root.right:
            count += 1
            root = root.right
        return count