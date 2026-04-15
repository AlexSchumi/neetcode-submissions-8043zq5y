class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        preMap = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            preMap[i].append(j)
        visit = set()

        def dfs(i):
            if i in visit:
                return False
            visit.add(i)
            for j in preMap[i]:
                if not dfs(j):
                    return False
                visit.remove(i)
            return True

        if not dfs(0):
            return []
        else:
            return []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        
        