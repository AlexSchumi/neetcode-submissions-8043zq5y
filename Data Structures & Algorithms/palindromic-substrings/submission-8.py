class Solution:
    # brute-force solution is done
    # runtime: O(N^3)
    # space: O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res

# optmized solution? two pointer?
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cur_len = len(s) - i

            if cur_len % 2 == 0:
                l, r = cur_len // 2, cur_len // 2
            else:
                l, r = cur_len // 2 - 1, cur_len // 2

            while l >= i and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

            

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            # =========================================================
            # 模式 1：奇数长度回文串（中心是一个字符，比如 "aba" 中的 'b'）
            # =========================================================
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1  # 左指针向左走
                r += 1  # 右指针向右走

            # =========================================================
            # 模式 2：偶数长度回文串（中心是两个字符的间隙，比如 "abba" 中的 "bb"）
            # =========================================================
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1  # 左指针向左走
                r += 1  # 右指针向右走
                
        return res

