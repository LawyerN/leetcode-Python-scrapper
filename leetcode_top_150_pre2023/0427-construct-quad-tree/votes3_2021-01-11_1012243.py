"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> \'Node\':
        
        \'\'\'
        Make a helper function helper(x, y, size) where x,y is coord of top left. 
        
        If size is 1, set val to grid[x][y], isLeaf true, and children to None.
        
        Create node for all children.
        
        If all children are leaves with same value, set same value, set isLeaf to True and children to None. 
        Otherwise value can be whatever, set isLeaf false.
        
        topleft : helper(x, y, size // 2)
        topright : helper(x, y + size // 2, size // 2)
        bottomleft: helper(x + size // 2, y, size // 2)
        bottomright: helper(x + size // 2, y + size // 2, size // 2)
        
        \'\'\'
        
        def helper(x, y, size):
            if size == 1:
                return Node(grid[x][y], True, None, None, None, None)
            
            half = size // 2
            topLeft = helper(x, y, half)
            topRight = helper(x, y + half, half)
            bottomLeft = helper(x + half, y, half)
            bottomRight = helper(x + half, y + half, half)
            
            children = [topLeft, topRight, bottomLeft, bottomRight]
            
            allLeaves = all(c.isLeaf for c in children)
            allMatch = all(c.val == topLeft.val for c in children)
            
            isLeaf = allLeaves and allMatch
            
            if isLeaf:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
            
        return helper(0, 0, len(grid))