class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        totals = []
        oldSums = []
        def helper(curr = root, level = 0):
            nonlocal ans, totals, oldSums
            if curr:
                if len(ans) > level:
                    total = totals[level] + 1
                    newSum = oldSums[level]+curr.val
                    ans[level] = round(newSum/total, 5)
                    oldSums[level] = newSum
                    totals[level] = total
                else:
                    ans.append(round(curr.val, 5))
                    totals.append(1)
                    oldSums.append(curr.val)
                helper(curr.left, level + 1)
                helper(curr.right, level + 1)
            return
        helper()
        return ans