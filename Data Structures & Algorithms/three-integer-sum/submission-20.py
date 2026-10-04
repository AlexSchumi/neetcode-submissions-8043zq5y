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
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]: # 1. Skip duplicate pivots for i
                continue # next loop

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    results.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return results

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort in-place O(N log N)
        results = []
        for i in range(len(nums) - 2):
            # Early exit: since array is sorted, if nums[i] > 0, three positive numbers cannot sum to 0
            if nums[i] > 0:
                break

            # 1. Skip duplicate pivots for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    results.append([nums[i], nums[l], nums[r]])

                    # 2. Skip duplicate left and right elements in O(1)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return results

        