class Solution:
    # brute force
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.helper(s[i:j]):
                    res += 1

        return res


    def helper(self, s: str) -> bool:
        return s == s[::-1]
        