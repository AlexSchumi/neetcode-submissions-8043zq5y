class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            # border reach
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0' # mark it as 0 so that do not visit again
            move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for move_row, move_col in move:
                dfs(i + move_row, j + move_col)
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1
        return islands





        