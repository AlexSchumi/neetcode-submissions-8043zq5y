# brutal-force solution
# runtime complexity: O(N^2)
# space complexity: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_str = s[i:j+1]
                if len(set(cur_str)) == len(cur_str):
                    res = max(len(cur_str), res)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r - l + 1, res)
        return res


        