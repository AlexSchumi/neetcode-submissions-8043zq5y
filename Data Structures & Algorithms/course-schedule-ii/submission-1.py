class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        
        output = [] # crs added to the output
        visit, cycle = set(), set() 

        def dfs(crs):
            if crs in cycle: #detect a cycle -> visiting twice
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for c in prereq[crs]:
                if dfs(c) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output
            
                
                

        