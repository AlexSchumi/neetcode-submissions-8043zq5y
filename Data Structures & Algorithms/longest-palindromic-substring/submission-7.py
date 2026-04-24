class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s

        res = ''
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                cur_str = s[i:j]
                if cur_str == cur_str[::-1] and len(cur_str) > len(res):
                    res = cur_str

        return res