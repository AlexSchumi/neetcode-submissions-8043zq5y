# DFS Solution;
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(start_idx):
            if start_idx >= len(nums) - 1:
                return True
            if nums[start_idx] == 0:
                return False
            if start_idx in memo:
                return memo[start_idx]
        
            max_step = nums[start_idx]
            end_idx = min(len(nums), start_idx + max_step + 1)

            for idx in range(start_idx + 1, end_idx):
                if dfs(idx):
                    memo[start_idx] = True
                    return True
            memo[start_idx] = False
            return False
        return dfs(0)

       
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        
        for i, jump in enumerate(nums):
            # 如果当前站的位置已经超过了你最远能走到的极限，说明你根本走不到这里
            if i > max_reachable:
                return False
            
            # 更新你能达到的最远边界
            max_reachable = max(max_reachable, i + jump)
            
            # 如果最远边界已经超越或到达了最后一个位置，提前通关 - this is understandable
            if max_reachable >= len(nums) - 1:
                return True
                
        return True

        