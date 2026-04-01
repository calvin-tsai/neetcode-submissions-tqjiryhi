class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            count = 1

            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if ((r, c) not in visit and
                        r >= 0 and c >= 0 and
                        c < cols and r < rows and 
                        grid[r][c] == 1):
                        visit.add((r, c))
                        q.append((r, c))
                        count += 1
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea
