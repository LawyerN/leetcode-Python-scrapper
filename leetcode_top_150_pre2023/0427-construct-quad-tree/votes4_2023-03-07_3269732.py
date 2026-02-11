class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        
        # Define a recursive function to construct the Quad-Tree
        def construct_helper(grid):
            # Check if the grid has length 1
            if len(grid) == 1:
                return Node(val=bool(grid[0][0]), isLeaf=True)
            
            # Check if all elements in the grid are the same
            all_same = all(all(val == grid[0][0] for val in row) for row in grid)
            if all_same:
                return Node(val=bool(grid[0][0]), isLeaf=True)
            
            # Otherwise, create a new node with isLeaf=False
            node = Node(isLeaf=False)
            
            # Divide the grid into four sub-grids
            n = len(grid)
            mid = n // 2
            top_left = [row[:mid] for row in grid[:mid]]
            top_right = [row[mid:] for row in grid[:mid]]
            bottom_left = [row[:mid] for row in grid[mid:]]
            bottom_right = [row[mid:] for row in grid[mid:]]
            
            # Recurse on each sub-grid and assign the resulting node to the appropriate child
            node.topLeft = construct_helper(top_left)
            node.topRight = construct_helper(top_right)
            node.bottomLeft = construct_helper(bottom_left)
            node.bottomRight = construct_helper(bottom_right)
            
            return node
        
        # Call the recursive function and return the root node
        return construct_helper(grid)