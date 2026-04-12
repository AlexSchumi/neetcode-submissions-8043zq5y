class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                return True
            visited.add(crs)

            for course in preMap[crs]:
                if not dfs(course): 
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True
            



        

        
        