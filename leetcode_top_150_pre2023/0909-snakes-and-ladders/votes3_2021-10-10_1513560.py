class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = collections.deque()
        n = len(board)
        queue.append((1, 0)) # (label, path_len)
        visited = set()
        
        def square_to_idx(val):
            row_idx = n - 1 - (val - 1) // n
            revert = True if (n - 1 - row_idx) % 2 == 1 else False
            col_idx = (val - 1) % n
            col_idx = n - 1 - col_idx if revert else col_idx
            return row_idx, col_idx
        
        while queue:
            cur_val, path_len = queue.popleft()
            visited.add(cur_val)
            cur_row, cur_col = square_to_idx(cur_val)
            # see a ladder/snake and move
            # note this doesn\'t take an extra step
            # so no need to add to the queue
            if board[cur_row][cur_col] != -1:
                cur_val = board[cur_row][cur_col]
            # game ends
            # note: cannot use cur_row = row_col == 0 
            # as the first row might be reverted
            if cur_val == n ** 2:
                return path_len
            # next move
            max_move = min(cur_val + 6, n ** 2)
            for dest_val in range(cur_val + 1, max_move + 1):
                if dest_val not in visited:
                    dest_row, dest_col = square_to_idx(dest_val)
                    queue.append((dest_val, path_len + 1))

        return -1