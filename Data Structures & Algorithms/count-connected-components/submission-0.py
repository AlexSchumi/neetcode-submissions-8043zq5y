class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        adj = {i:[] for i in range(n)}
        for i, j in edges: # store all paths
            adj[i].append(j)
            adj[j].append(i)
        visited = [False] * n

        def dfs(i):
            '''
            if i in visited:
                return
            
            visited.add(i)
            for j in paths[i]:
                if j not in visited:
                    dfs(j)
            '''
            for nei in adj[i]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res

                    

        