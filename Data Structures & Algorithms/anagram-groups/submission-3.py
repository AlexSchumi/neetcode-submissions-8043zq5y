class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = [[strs[0]]]

        for i in range(1, len(strs)):
            _str = strs[i]
            flag = False
            for result in results:
                if self.isAnagrams(_str, result[0]):
                    result.append(_str)
                    flag = True
                    break
            if not flag:
                results.append([_str])
        return results


    def isAnagrams(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)

        