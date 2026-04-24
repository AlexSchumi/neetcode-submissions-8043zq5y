class Solution:
    # use dfs (top-down)
    def climbStairs(self, n: int) -> int:
        memory = [-1] * (n+1)

        def dfs(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            
            if memory[i] != -1:
                return memory[i]
            else:
                memory[i] = dfs(i-2) + dfs(i-1)
                return memory[i]
                
        res = dfs(n)
        return res
    

    # use bottom up solution;
    # space complexity: O(N)
    # runtime complexity: O(N)
    '''
    def climbStairs(self, n: int) -> int:
        memory = [0] * (n+1)
        memory[0] = 1
        memory[1] = 1

        # everytime, you climb 2 stairs or 1 stair;
        for i in range(2, n+1):
            memory[i] = memory[i-2] + memory[i-1]
        
        return memory[-1]
    '''


    


        