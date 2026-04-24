class Solution:
    # use dfs (top-down)
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i <= 0:
                return 0
            return dfs(i-2) + dfs(i-1) + 1
        res = dfs(n)
        return res
    
    # use bottom up solution;
    def climbStairs(self, n: int) -> int:
        memory = [0] * (n+1)
        memory[0] = 1
        memory[1] = 1
        for i in range(2, n+1):
            memory[i] = memory[i-2] + memory[i-1]
        
        return memory[-1]


    


        