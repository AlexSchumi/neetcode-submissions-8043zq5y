class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()

        def dfs(res, cur_num, visited):
            if len(res) > len(nums):
                return
            if cur_num == len(nums):
                results.append(res)

            for num in nums:
                if num in visited:
                    continue
                else:
                    visited.add(num)
                    dfs(res+[num], cur_num+1, visited)
                    visited.remove(num)
        dfs([], 0, visited)
        return results
        


        