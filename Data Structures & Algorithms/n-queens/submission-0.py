class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # first instict: brute force approach is to recursively place a queen, eliminate attacked tiles, then place another queen, if there is no place for a queen to go then pop back up but if a result has been found then +1 to result. 

        # recursive backtracking: keep track of sets for col, posDiag, negDiag at each selection.
        # row by row, choose a valid Q location

        cols = set()
        negDiag = set() # r - c
        posDiag = set() # r + c

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # means we have reached end state: Only possible after valid queen combination is found
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
    
            # find a valid column in the given row
            for c in range(n):
                if c in cols or (r - c) in negDiag or (r + c) in posDiag:
                    continue
            
                # add
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # explore
                backtrack(r + 1)

                # un-add
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res





        