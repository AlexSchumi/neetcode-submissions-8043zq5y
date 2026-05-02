class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break          
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l >= 0 and r < len(nums) and l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
        return res

