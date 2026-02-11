class Solution:
    def buildTreeHelper(self, postorder: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        root_value = postorder[self.postorder_index]
        self.postorder_index -= 1
        root = TreeNode(root_value)
        inorder_pivot_index = self.inorder_index_map[root_value]
        root.right = self.buildTreeHelper(postorder, inorder_pivot_index + 1, right)
        root.left = self.buildTreeHelper(postorder, left, inorder_pivot_index - 1)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder_index = len(postorder) - 1
        self.inorder_index_map = {val: i for i, val in enumerate(inorder)}
        return self.buildTreeHelper(postorder, 0, len(postorder) - 1)