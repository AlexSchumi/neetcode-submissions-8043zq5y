class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []

        def dfs(cur_res, index):
            if sum(cur_res) == target:
                res.append(cur_res[:])
                return res

            if sum(cur_res) > target:
                return res
            
            for i in range(len(nums)):
                cur_res.append(nums[i])
                dfs(cur_res, i)
                cur_res.pop(-1)
            return res
        dfs([], 0)
        return len(res)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            
            if remain in memo:
                return memo[remain]
            
            res = 0
            for num in nums:
                res += dfs(remain - num)
            
            memo[remain] = res
            return res

        return dfs(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            
            if remain in memo:
                return memo[remain]
            res = 0
            for num in nums:
                res += dfs(remain - num)

            memo[remain] = res
            return res
        
        return dfs(target)
            

        