# dfs solution
# runtime complexity:
# space complexity: 
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        memo = set()
        
        def dfs(cur_res, start_idx):
            if sum(cur_res) > target:
                return

            if sum(cur_res) == target: # how to deduplicate????
                results.append(cur_res[::])
                return
            
            for j in range(start_idx, len(nums)):
                dfs(cur_res + [nums[j]], j)

        dfs([], 0)
        return results
                
        