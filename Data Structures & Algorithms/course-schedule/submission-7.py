from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        in_degree = [0] * numCourses
        for crs, pre_crs in prerequisites:
            pre[pre_crs].append(crs)
            in_degree[crs] += 1

        # 0 in degree course as a starting point to iterate over
        q = deque()
        for n in range(numCourses):
            if in_degree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in pre[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return finish == numCourses

        
        