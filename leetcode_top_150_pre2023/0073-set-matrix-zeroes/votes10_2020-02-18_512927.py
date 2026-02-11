class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        h, w = len( matrix), len( matrix[0])
        
        row_mask, col_mask = 0, 0
        
        ## Step_#1
        #
        # Setup masking for zero element
        for y in range(h):
            for x in range(w):
                
                if matrix[y][x] == 0:
                    
                    row_mask |= (1<<y)
                    col_mask |= (1<<x)
        
        
        ## Step_#2
        #
        # Clear by row mask and column mask
        for y in range(h):
            for x in range(w):
                
                if row_mask & (1<<y) or col_mask & (1<<x):
                    matrix[y][x] = 0