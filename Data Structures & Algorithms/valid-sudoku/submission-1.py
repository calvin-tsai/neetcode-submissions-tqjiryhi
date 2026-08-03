class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force: for square, check row, col, block
        # visit set for 9 blocks, 9 row, 9 cols
        # block1: {1, 2, 3, 5}

        ROWS, COLS = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                # if number, add it to respective row, col, block set
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in blocks[(r // 3, c // 3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                blocks[(r // 3, c // 3)].add(board[r][c])
                
                # if any of these 3 sets already have the number, return false

        return True