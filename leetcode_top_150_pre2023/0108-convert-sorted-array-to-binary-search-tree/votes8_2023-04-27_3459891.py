class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        n = len(nums)
        root = TreeNode()
        stack = [(0, n, root)]
        
        while stack:
            i, j, node = stack.pop()
            mid = (i + j) // 2
            node.val = nums[mid]
            
            if mid > i:
                node.left = TreeNode()
                stack.append((i, mid, node.left))
            if mid+1 < j:
                node.right = TreeNode()
                stack.append((mid+1, j, node.right))
                
        return root