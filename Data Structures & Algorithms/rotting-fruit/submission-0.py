class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs

        # keep track of time
        # count number of 1s
        # if q is empty and there are 1s left, return -1 else return time

        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(ROWS): # count number of 1s, append all coordinates with a 2
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: # if no fresh, no need to do bfs
            return 0

        time = 0
        while fresh > 0 and q:
            len_q = len(q)
            for i in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row >= 0 and col >= 0 and
                        row < ROWS and col < COLS and
                        grid[row][col] == 1
                    ):
                        fresh -= 1
                        grid[row][col] = 2
                        q.append((row, col))
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1




