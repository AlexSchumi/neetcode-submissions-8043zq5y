class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        charset = set()
        l = 0
        # sliding window usually increase right, narrow down left to find correct condition
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            res = max(res, r - l + 1)
        return res

                
