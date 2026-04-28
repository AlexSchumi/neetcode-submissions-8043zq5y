# already solved by brute force solution and this is my optimized solution;
class Solution:
    # optimized solution
    # runtime complexity: O(N^3)
    # space complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    res += 1
        return res
        
        