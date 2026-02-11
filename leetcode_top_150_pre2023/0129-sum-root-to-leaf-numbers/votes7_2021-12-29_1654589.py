def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(cur_node: Optional[TreeNode], num: int):
            if not cur_node.left and not cur_node.right:
                self.ans += num * 10 + cur_node.val
                return
            
            if cur_node.left:
                dfs(cur_node.left, num * 10 + cur_node.val)
            
            if cur_node.right:
                dfs(cur_node.right, num * 10 + cur_node.val)
            
        dfs(root, 0)
        
        return self.ans