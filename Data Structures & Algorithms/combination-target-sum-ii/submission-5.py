class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def dfs(res, cur_sum, start_idx):
            if cur_sum == target:
                results.append(res)
                return

            if cur_sum > target:
                return

            for idx in range(start_idx, len(candidates)):
                # Skip duplicate elements at the same recursion level
                if idx > start_idx and candidates[idx] == candidates[idx - 1]:
                    continue
                dfs(res + [candidates[idx]], cur_sum + candidates[idx], idx + 1)

        dfs([], 0, 0)
        return results
        