class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return # empty board
    m, n = len(board), len(board[0])
    
    def dfs(i: int, j: int) -> None:
        """
        Depth-first search function to mark all O\'s connected to the current O (i, j).
        """
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != \'O\':
            return
        
        board[i][j] = \'#\'  # mark as visited
        
        # recursively mark all adjacent O\'s
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        
    # mark all O\'s on the edges
    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)
        
    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)
        
    # flip unvisited O\'s to X\'s and marked O\'s back to O\'s
    for i in range(m):
        for j in range(n):
            if board[i][j] == \'O\':
                board[i][j] = \'X\'
            elif board[i][j] == \'#\':
                board[i][j] = \'O\'