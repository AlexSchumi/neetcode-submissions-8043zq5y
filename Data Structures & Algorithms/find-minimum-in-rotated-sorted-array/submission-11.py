# hahahahaha????
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
'''
        