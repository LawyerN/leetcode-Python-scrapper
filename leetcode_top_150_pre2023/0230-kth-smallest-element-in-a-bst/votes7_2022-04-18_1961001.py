class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        arr = self.inorder(root,values)
        return arr[k-1]
    
    #Driver Function For Inorder Traversal
	#Inorder Traversal means Left -> Root -> Right
	
    def inorder(self,root,a):
        if(root):
            self.inorder(root.left,a)
            a.append(root.val)  #Storing The Values in the Array which is passed as an argument
            self.inorder(root.right,a)
        return a