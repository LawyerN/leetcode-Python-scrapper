def spiral_order(matrix)
  (row = matrix.shift) ? row + spiral_order(matrix.transpose.reverse) : []
end