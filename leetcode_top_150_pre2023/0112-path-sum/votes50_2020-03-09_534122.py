def hasPathSum(self, root: TreeNode, sum: int) -> bool:
	if not root:
		return False
	if not root.left and not root.right and root.val == sum:
		return True
	return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)