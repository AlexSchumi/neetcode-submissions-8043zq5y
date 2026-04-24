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



        


class Solution:
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
















        