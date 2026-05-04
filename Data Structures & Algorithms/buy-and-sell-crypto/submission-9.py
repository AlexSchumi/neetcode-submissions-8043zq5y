# brute force solution
# runtime complexity: O(N^2)
# space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res

# Optimized Solution
# runtime complexity: O(N)
# space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0

        while j < len(prices) and i < len(prices) and i < j:
            if prices[i] >= prices[j]:
                #i += 1
                #j += 1
                i = j
            else:
                profit = prices[j] - prices[i]
                res = max(profit, res)
            j += 1

        return res

