class Solution:
    #brutal-force solution here
    #space complexity: O(1)
    #runtime complexity: O(N^3)
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        res = ''
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                cur_str = s[i:j]
                if cur_str == cur_str[::-1] and len(cur_str) > len(res):
                    res = cur_str
        return res


#optimized DP solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        reslen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l: r+1]
                    reslen = len(res)
                l -= 1
                r += 1
            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l: r+1]
                    reslen = len(res)
                l -= 1
                r += 1
        
        return res

