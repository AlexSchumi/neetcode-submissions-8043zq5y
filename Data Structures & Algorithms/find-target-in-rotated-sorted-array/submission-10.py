class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            # Case 1: Left half is strictly sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is in the left sorted portion
                else:
                    l = m + 1  # Target is in the right portion
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is in the right sorted portion
                else:
                    r = m - 1  # Target is in the left portion

        return -1