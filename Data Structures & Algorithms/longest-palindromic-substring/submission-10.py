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
        