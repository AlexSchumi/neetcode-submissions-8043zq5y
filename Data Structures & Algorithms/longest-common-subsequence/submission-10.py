class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)

            return max(dfs(i+1, j), dfs(i, j+1))

        return dfs(0, 0)
        
# Top-Down Recurssion Solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            res = max(dfs(i+1, j), dfs(i, j+1))
            memo[(i, j)] = res
            return res

        return dfs(0, 0)

# Bottom-up solution below:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]

        
        