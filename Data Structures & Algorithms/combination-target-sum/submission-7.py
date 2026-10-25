class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []

        def dfs(res, start_idx, cur_sum):
            if cur_sum == target:
                results.append(res)

            if cur_sum > target:
                return

            for idx in range(start_idx, len(nums)):
                dfs(res+[nums[idx]], idx, cur_sum + nums[idx])

        dfs([], 0, 0)

        return results


            
        