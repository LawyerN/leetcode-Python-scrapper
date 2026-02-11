class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = dict()
        def bfs(curr=root, level = 0):
            nonlocal ans
            if curr != None:
                if level % 2 == 1: # go right to left, used stack
                    if level in ans.keys():
                        ans[level].insert(0, curr.val)
                    else:
                        ans[level] = [curr.val]
                else: #go left to right, used queue
                    if level in ans.keys():
                        ans[level].append(curr.val)
                    else:
                        ans[level] = [curr.val]
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)
            return
        bfs()
        return ans.values()