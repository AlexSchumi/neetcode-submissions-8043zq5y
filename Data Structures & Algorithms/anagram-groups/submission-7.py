class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if len(strs) == 1:
            return [strs]
        
        for s in strs:
            if len(res) == 0:
                res.append([s])
            else:
                find_anagram = False
                for r in res:
                    if self.isAnagrams(s, r[0]):
                        find_anagram = True
                        r.append(s)
                        break
                if not find_anagram:
                    res.append([s])
        return res

    def isAnagrams(self, str1, str2) -> bool:
        if len(str1) != len(str2):
            return False
        t1 = defaultdict(str)
        
        for s1 in str1:
            t1[s1] = t1.get(s1, 0) + 1
        for s2 in str2:
            t1[s2] = t1.get(s2, 0) - 1

        for val in t1.values():
            if val != 0:
                return False
        return True
        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            results[tuple(count)].append(s)
        return list(results.values())
                




        

        