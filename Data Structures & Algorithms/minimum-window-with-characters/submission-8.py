class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target_count = {}
        for _t in t:
            target_count[_t] = target_count.get(_t, 0) + 1

        l, res = 0, 0
        flag = False

        for r in range(len(s)-1, -1, -1): #shrink the window
            # move right until find the substring
            if s[r] in target_count:
                target_count[s[r]] -= 1
            
            while l < r and all(target_count.values()) <= 0: #find the string
                res_string = s[l:r+1]
                flag = True
                #shrink left pointer
                if s[l] in target_count:
                    target_count[s[l]] -= 1
                else:
                    if r - l + 1 < res:
                        res_string = s[l:r+1]
                l += 1

        if not flag:
            return ""
        else:
            return res_string
                

class Solution:
    '''
    1. First step: move right pointer to find qualifier
    2. If it is qualified, move left pointer to shrink the window to find the minimum
    3. Update window/length
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT, window = {}, {}
        for _t in t:
            countT[_t] = countT.get(_t, 0) + 1

        res = [-1, -1]
        resLen = float("inf")
        need = len(countT)
        have = 0
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1 # i have met the criterion of character s[r]

            while have == need: #condition met
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""





            

            
        

        