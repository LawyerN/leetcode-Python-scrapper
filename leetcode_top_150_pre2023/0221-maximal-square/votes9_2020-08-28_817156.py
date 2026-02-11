class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        maxRows = len(matrix)
        maxCols = len(matrix[0])
        maxLength = 0
        for i in range(maxRows):
            for j in range(maxCols):
                if matrix[i][j] == \'1\':
                    length = self.getLength(matrix, i, j, maxRows, maxCols)
                    maxLength = max(length, maxLength)
        return maxLength**2
        
    def getLength(self, matrix, row, col, maxRows, maxCols):
        # We can get away with simple \'and\' condition as the matrix is always square and never a rectangle
        if 0 <= row < maxRows and 0 <= col < maxCols:
            if matrix[row][col] == \'1\':
                return 1 + min(
                                self.getLength(matrix, row+1, col, maxRows, maxCols),
                                self.getLength(matrix, row, col+1, maxRows, maxCols),
                                self.getLength(matrix, row+1, col+1, maxRows, maxCols)
                              )
            
        # if we are at the end of array or matrix[i][j] is zero, we don\'t have to explore further and we can return 0
        return 0