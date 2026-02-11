class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = [], []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)
        
        for r in row:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0