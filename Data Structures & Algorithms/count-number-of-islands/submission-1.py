class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(i, j):
            visit = set()
            q = collections.deque()
            q.append((i, j))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0"):
                        continue
                    q.append((row, col))
                    grid[row][col] = "0"
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        
        return islands
                    
