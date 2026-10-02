class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        left_res = 1
        for i in range(1, len(nums)):
            left[i] = left_res * nums[i-1]
            left_res = left[i]

        right_res = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right_res * nums[i+1]
            right_res = right[i]

        results = [1] * len(nums)
        for i in range(len(nums)):
            results[i] = left[i] * right[i]

        return results

        