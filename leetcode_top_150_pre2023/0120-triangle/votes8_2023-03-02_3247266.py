#RECURSION
class Solution1(object):
    def minimumTotal(self, triangle):
        l = len(triangle)
        def solve(row,idx):
            if row == l-1:
                return triangle[row][idx]
            return triangle[row][idx]+min(solve(row+1,idx),solve(row+1,idx+1))
        ans = solve(0,0)
        return ans

#MEMOIZATION
class Solution2(object):
    def minimumTotal(self, triangle):
        l = len(triangle)
        memo = [[-1 for i in range(len(triangle[j]))] for j in range(len(triangle))]
        #print(memo) 
        def solve(row,idx):
            if row == l-1:
                return triangle[row][idx]
            if memo[row][idx] != -1:
                return memo[row][idx]
            memo[row][idx] = triangle[row][idx]+min(solve(row+1,idx),solve(row+1,idx+1))
            return memo[row][idx]
        ans = solve(0,0)
        return ans

#TABULATION (Top Down)
class Solution3(object):
    def minimumTotal(self, triangle):
        l = len(triangle)
        memo = [[-1 for i in range(len(triangle[j]))] for j in range(len(triangle))]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    memo[i][j] = triangle[i][j]
                else:
                    if j<i and j-1>=0:
                        memo[i][j] = triangle[i][j]+min(memo[i-1][j],memo[i-1][j-1])
                    elif j<i:
                        memo[i][j] = triangle[i][j] + memo[i-1][j]
                    elif j-1>=0:
                        memo[i][j] = triangle[i][j] + memo[i-1][j-1]

      
        return min(memo[-1])

#SPACE OPTIMIZATION
class Solution(object):
    def minimumTotal(self, triangle):
        l = len(triangle)
        for i in range(l-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]