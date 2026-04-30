'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicts = {}
        for num in nums:
            if num in dicts:
                return True
            else:
                dicts[num] = 1
        return False
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
