class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)  # Recursively flatten the right subtree
        self.flatten(root.left)  # Recursively flatten the left subtree
        root.right = self.prev  # Set the right child to the previously flattened node
        root.left = None  # Set the left child to None
        self.prev = root  # Update the previously flattened node to be the current node