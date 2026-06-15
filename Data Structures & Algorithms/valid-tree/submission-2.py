class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit: # circle detected
                return False
                
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit: 
                    return False # 踩过且不是亲爹，铁证如山，这就是真实的环！
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n



        