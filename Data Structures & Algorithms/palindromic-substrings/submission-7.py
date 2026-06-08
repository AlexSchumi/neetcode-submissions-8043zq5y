class Solution:
    # brute-force solution
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res

