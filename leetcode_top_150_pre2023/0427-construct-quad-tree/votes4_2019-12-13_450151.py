def is_leaf(self, grid, u_r, u_c, l_r, l_c):
        val = grid[u_r][u_c]
        
        for r in range(u_r, l_r):
            for c in range(u_c, l_c):
                if grid[r][c] != val:
                    return False
        return True
    
def build_quad(self, grid, u_r, u_c, l_r, l_c):
    if self.is_leaf(grid, u_r, u_c, l_r, l_c):
        val = grid[u_r][u_c]
        return Node(val, True, None, None, None, None)
    
    m_r = u_r + ((l_r - u_r) // 2)
    m_c = u_c + ((l_c - u_c) // 2)
        
    topLeft = self.build_quad(grid, u_r, u_c, m_r, m_c)
    bottomLeft = self.build_quad(grid, m_r, u_c, l_r, m_c)
    topRight = self.build_quad(grid, u_r, m_c, m_r, l_c)
    bottomRight = self.build_quad(grid, m_r, m_c, l_r, l_c)    
    
    return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)

def construct(self, grid: List[List[int]]) -> \'Node\':
    n = len(grid)
    return self.build_quad(grid, 0, 0, n, n)