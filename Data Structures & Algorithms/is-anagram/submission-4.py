class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for _s in s:
            if _s not in dict1:
                dict1[_s] = 1
            else:
                dict1[_s] += 1
        
        for _t in t:
            if _t not in dict1:
                return False
            else:
                dict1[_t] -= 1
        
        for k, v in dict1.items():
            if v != 0:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)       