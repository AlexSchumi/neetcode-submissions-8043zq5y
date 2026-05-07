class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxf = 0
        count = {}
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(count[s[j]], maxf)
                if (j - i + 1) - maxf <= k:
                    res = max(j - i + 1, res)
        return res