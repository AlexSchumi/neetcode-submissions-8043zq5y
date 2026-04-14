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
# Time complexity: O(V+E)
# Space complexity: O(V+E)

# BFS Solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # same solution here
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res
                    

        