class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_str = s[i:j+1]
                if len(set(cur_str)) == len(cur_str):
                    res = max(len(cur_str), res)
        return res

        