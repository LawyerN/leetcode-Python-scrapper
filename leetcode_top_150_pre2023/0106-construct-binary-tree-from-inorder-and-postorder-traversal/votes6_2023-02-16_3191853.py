class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Use a hashmap to store the indices of each element in the inorder list
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        
        # Define a recursive helper function to build the tree
        def build(start, end):
            # Base case: the start index is greater than the end index
            if start > end:
                return None
            
            # Create a new node with the last value in the postorder list
            val = postorder.pop()
            node = TreeNode(val)
            
            # Find the index of the node in the inorder list
            index = inorder_map[val]
            
            # Recursively build the right subtree first, since we\'re working with the postorder traversal
            node.right = build(index + 1, end)
            # Then build the left subtree
            node.left = build(start, index - 1)
            
            return node
        
        # Call the helper function to build the tree
        return build(0, len(inorder) - 1)