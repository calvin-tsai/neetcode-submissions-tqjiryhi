class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # initialize queue and global variables
        q = deque()
        time, fresh = 0, 0

        # iterate through each cell once, O(n * m) to figure out what is happening
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1  # this will find all fresh oranges initially
                if grid[r][c] == 2:
                    q.append([r, c])  # if we find a rotten orange, this is a source

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # continue this loop while we still have rotten source and still fresh oranges left
        while q and fresh > 0:

            # takes a snapshot. only iterates the number of times len(q) is initially
            # even if the q increases in length - important for days inc!
            for i in range(len(q)): 
                r, c = q.popleft() # current row, col of rotten
                for dr, dc in directions:
                    row, col = dr + r, dc + c # 1 of 4 adjacent row col
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2 # change the grid
                    q.append([row, col])
                    fresh -= 1
            # one day = one full run of the queue (not including new rotten)
            time += 1
        
        return time if fresh == 0 else -1




