from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = defaultdict(str)

        for _s in s:
            char_dict[_s] = char_dict.get(_s, 0) + 1

        for _t in t:
            char_dict[_t] = char_dict.get(_t, 0) - 1


        for val in char_dict.values():
            if val != 0:
                return False

        return True



        