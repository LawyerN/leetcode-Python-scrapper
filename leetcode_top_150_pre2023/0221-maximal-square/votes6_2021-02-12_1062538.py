class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        #dp = [[0] * n for _ in range(m)]
        
        #dp[i][j] looks at topleft,top,left values
        #since there\'s no rules about modifying input matrix, we can use our input matrix as our dp matrix to be memory efficient
        
        #initialize maxSquareSide to be 0 (or 1 if there\'s a 1 in first row or col)
        maxSquareSide = 0 #our current max square side length
        for val in matrix[0]:
            #first row
            if val == "1":
                maxSquareSide = 1
                break
        if maxSquareSide == 0:
            for i in range(m):
                #first col
                if matrix[i][0] == "1":
                    maxSquareSide = 1
                    break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    matrix[i][j] = str(min(int(matrix[i-1][j-1]),int(matrix[i-1][j]),int(matrix[i][j-1])) + 1)
                if int(matrix[i][j]) > maxSquareSide:
                    maxSquareSide = int(matrix[i][j])
        #print(matrix)
        return maxSquareSide**2