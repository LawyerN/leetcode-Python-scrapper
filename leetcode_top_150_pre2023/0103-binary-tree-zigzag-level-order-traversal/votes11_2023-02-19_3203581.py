# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Level traversal -> BFS
    # reverse the list for odd-index level
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if there is no root, then return []
        if not root: return []
        # init ans and queue with initial node `root`
        ans, q = [], [root]
        # BFS
        while q:
            # direction - 1 for even-index level and -1 for odd-index level
            d = -1 if len(ans) % 2 == 1 else 1
            # put all node values to a list with the correct direction 
            # and add to `ans` 
            ans.append([n.val for n in q][::d])
            # for each node in the queue, 
            # we add the left or right node to the queue if applicable
            q = [n for node in q for n in (node.left, node.right) if n]
        return ans