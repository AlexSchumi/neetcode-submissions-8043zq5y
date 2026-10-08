class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        target, window = {}, {}
        for _t in t:
            target[_t] = target.get(_t, 0) + 1
        
        resLen = float("inf")
        res = [-1, -1]
        need = len(target)
        l, have = 0, 0


        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen: #update first
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        l, r = res
                
        return s[l:r+1] if resLen != float("inf") else ""
