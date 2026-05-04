class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i, j = 0, 1
        word_map = set()
        word_map.add(s[i])
        res = 1
        while j < len(s) and i < len(s) and i < j:
            if s[j] not in word_map:
                word_map.add(s[j])
                res = max(len(word_map), res)
            else:
                word_map = set()
                i = j
                word_map.add(s[i])
            j += 1
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        word_set = set()
        res = 0

        for j in range(len(s)):
            while s[j] in word_set:
                # 我们就从左边移除字符，直到窗口里不再有 s[j]
                word_set.remove(s[i])
                i += 1
            # 现在的窗口肯定没有重复的 s[j] 了，把它加进去
            word_set.add(s[j])

            # 计算当前窗口的大小 (j - i + 1)
            res = max(res, j - i + 1)
            
        return res


        