class Solution:
    def __init__(self):
        # Map with key as level of the tree,
        # map[level] = {sum of the level, number of elements in the level}
        self.mp = defaultdict(lambda: [0.0, 0.0])

    # Function to calculate the sum and count of nodes at each level
    def avg(self, root: TreeNode, l: int) -> None:
        # If the node is a leaf node, return
        if not root:
            return

        # Add the current value to the sum of this level
        self.mp[l][0] += root.val

        # Increase the number of elements in the current level
        self.mp[l][1] += 1

        # Traverse left subtree
        self.avg(root.left, l + 1)

        # Traverse right subtree
        self.avg(root.right, l + 1)

    # Function to compute the average of levels in a binary tree
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # Resultant list
        ans = []

        # Calculate sum and count of nodes at each level
        self.avg(root, 0)

        # Iterate over the map to compute the average at each level
        for level, (sum_level, count) in sorted(self.mp.items()):
            ans.append(sum_level / count)

        return ans