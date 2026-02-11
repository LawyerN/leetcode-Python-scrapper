class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(mat),len(mat[0])
        r=c=0
#Storing the index of 0th element in first row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    if i==0:
                        r=1
                    if j==0:
                        c=1   
                    mat[i][0]=mat[0][j]=0
        
#If first row or column is marked with 0 the then marking all the elements in that row or column as 0
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][0]==0 or mat[0][j]==0:
                    mat[i][j]=0
#If first row or column as 0 then making all elements in first row or column as 0
        if r==1:
            for j in range(n):
                mat[0][j]=0
        if c==1:
            for i in range(m):
                mat[i][0]=0