def inorder(node: Optional[TreeNode]) -> Generator[int, None, None]:
    """
    Generator function that takes the root node of a binary tree
    and iterates through the nodes of the tree via inorder traversal.
    @param node - The root node of the binary tree.
    """
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)