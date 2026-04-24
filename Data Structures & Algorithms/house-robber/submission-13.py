class Solution:
    def rob(self, nums: List[int]) -> int:
        # work on 1/11/2026
        n = len(nums) + 1
        dp = [0] * n # set dp memory array to iterate
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = nums[1]

        # difficult part is to exclude 0 and 1 here
        for i in range(3, n):
            if i != n-1:
                if i == 3:
                    dp[i] = dp[i-2] + nums[i-1]
                else:
                    dp[i] = max(dp[:i-1]) + nums[i-1]
            else: # i == n-1
                dp[i] = max(dp[1:i-1]) + nums[i-1]
        return max(dp)

        






class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(dp[0] + nums[2], dp[1])



        for i in range(3, n):
            dp[i] = max(dp[:i-1]) + nums[i]
            
        return max(dp)






        




        