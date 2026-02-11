def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == \'O\' and (i in [0,len(board)-1] or j in [0,len(board[0])-1]):
                    DFS(i,j) # or BFS(i,j)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == \'O\':
                    board[i][j] = \'X\'
                if board[i][j] == \'D\':
                    board[i][j] = \'O\'