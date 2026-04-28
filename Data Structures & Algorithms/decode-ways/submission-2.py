class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' or not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 # 基础：空字符串有一种解码方式
        dp[1] = 1 # 已经排除首位为0，所以第1位必有1种
        
        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            two_digits = s[i-2:i]
            if 10 <= int(two_digits) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
                










        