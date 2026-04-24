class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        n = len(nums)
        if n == 1: 
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums:List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        # FIXED: Must be max of robbing house 0 or house 1
        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]



        
# space complexity: O(N)
# runtime complexity: O(N)
class Solution:
    # use bottom-up solution
    def rob(self, nums: List[int]) -> int:
        # do two round of finding robbery
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        max1 = self.helper(nums[1:])
        max2 = self.helper(nums[:len(nums)-1])

        return max(max1, max2)


    def helper(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]


class Solution:
    # use top-down solution - recursion solution
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo = {}

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1): # rob the first one and arrive the last house
                return 0
            state = (i, flag)
            if state in memo:
                return memo[state]
            
            res = max(dfs(i+1, flag), dfs(i+2, flag or i ==0) + nums[i])
            memo[state] = res
            return res
        
        return max(dfs(0, True), dfs(1, False))

















        