class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            current = node.right
            while current:
                self.stack.append(current)
                current = current.left
        return node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0