class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rigthElements = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            rigthElements.append(node.val)

        return rigthElements