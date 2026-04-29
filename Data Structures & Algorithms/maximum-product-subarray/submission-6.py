class Solution:
    # runtime complexity: O(N^2)
    # space complexity: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        for i in range(len(nums)):
            cur_value = nums[i]
            if cur_value > res:
                res = cur_value
            for j in range(i+1, len(nums)):
                cur_value = cur_value * nums[j]

                if cur_value > res:
                    res = cur_value
        return res

# DP solution to optimize
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            tmp = curmax * n
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(tmp, n * curmin, n)
            res = max(curmax, res)

        return res

        