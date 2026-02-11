def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    if board[i][j]==\'O\':
                        board[i][j]=\'Y\'
                        q.append((i,j))   
        while q:
            a,b=q.popleft()
            for r,c in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
                if 0<=r<m and 0<=c<n and board[r][c]==\'O\':
                    board[r][c]="Y"
                    q.append((r,c))
        for i in range(m):
            for j in range(n):
                if board[i][j]==\'O\':
                    board[i][j]=\'X\'
                elif board[i][j]==\'Y\':
                    board[i][j]=\'O\'