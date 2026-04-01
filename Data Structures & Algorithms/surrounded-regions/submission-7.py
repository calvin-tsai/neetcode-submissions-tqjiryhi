class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # iterate through the board's edges. If there is an O, mark it to not be changed.
        # do a dfs on that O and mark all adjacent edges to be unchanged
        # all uncircumcised Os be changed to Xs

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(ROWS): # top and bottom column
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        
