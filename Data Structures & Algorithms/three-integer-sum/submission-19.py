class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) <= 2:
            return []
        nums = sorted(nums)
        results = []

        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]: # if nums[i] == nums[i-1] skip
                continue #next loop

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if [nums[i], nums[l], nums[r]] not in results:
                        results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return results


        