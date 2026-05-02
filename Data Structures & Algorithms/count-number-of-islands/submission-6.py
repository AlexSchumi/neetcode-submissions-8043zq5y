class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            # border reach
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
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
            






        