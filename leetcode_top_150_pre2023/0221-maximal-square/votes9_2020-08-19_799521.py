def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        def helper(row, col):
            if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == \'0\':
                return 0
            return 1+min(helper(row+1, col), helper(row, col+1), helper(row+1, col+1))
        
        
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, helper(r,c))
        return res**2