class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0" or visited[i][j]:
                # If the current cell is out of bounds or is water (0) or has already been visited, return.
                return
            visited[i][j] = True # Mark the current cell as visited.
            dfs(i+1, j) # Visit the neighbor to the right.
            dfs(i-1, j) # Visit the neighbor to the left.
            dfs(i, j+1) # Visit the neighbor below.
            dfs(i, j-1) # Visit the neighbor above.
        
        m, n = len(grid), len(grid[0]) # Get the dimensions of the given matrix.
        visited = [[False for _ in range(n)] for _ in range(m)] # Initialize a visited matrix with False for all cells.
        count = 0 # Initialize a count variable to 0.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]: # If we encounter an unvisited 1, increment the count and perform a DFS on its neighbors, marking all the visited 1\'s as visited.
                    count += 1
                    dfs(i, j)
        return count # Return the count of the number of islands.