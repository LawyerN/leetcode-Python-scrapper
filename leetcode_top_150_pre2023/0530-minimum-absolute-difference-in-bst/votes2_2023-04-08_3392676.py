class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            nonlocal nums
            if root:
                helper(root.left)
                nums.append(root.val)
                helper(root.right)
        
        nums = []
        helper(root)
        
        return min(nums[i+1] - nums[i] for i in range(len(nums) - 1))