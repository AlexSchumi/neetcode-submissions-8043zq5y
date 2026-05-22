# brute-force solution version
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_string = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if j - i + 1 >= res:
                        res_string = s[i:j+1]
                        res = max(res, j - i + 1)
        return res_string

# Optimized Solution;
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx : resIdx + resLen]




        