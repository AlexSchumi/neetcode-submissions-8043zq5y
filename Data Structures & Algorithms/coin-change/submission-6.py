class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo: return memo[rem]
            res = float('inf') # 先假设需要无穷多个
            
            for coin in coins:
                sub_problem = dfs(rem - coin)

                if sub_problem != -1:
                    res = min(res, sub_problem + 1)

            memo[res] = res if res != float('inf') else -1
            return memo[res]
        
        res = dfs(amount)
        return res

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1



    
