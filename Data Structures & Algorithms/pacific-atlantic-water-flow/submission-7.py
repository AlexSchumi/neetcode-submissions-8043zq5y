class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        atlvisit = set()
        pacvisit = set()

        def dfs(r, c, visited, cur_min):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < cur_min:
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            return

        for i in range(rows):
            dfs(i, 0, pacvisit, heights[i][0]) 
            dfs(i, cols-1, atlvisit, heights[i][cols-1])
        
        for j in range(cols):
            dfs(0, j, pacvisit, heights[0][j]) 
            dfs(rows-1, j, atlvisit, heights[rows-1][j])
        
        res = []
        for atl in atlvisit:
            if atl in pacvisit:
                res.append(atl)
        return res


        