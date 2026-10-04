class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res_profit = 0

        for r in range(1, len(prices)):
            sell_price = prices[r]
            l = 0

            while l < r:
                buy_price = prices[l]
                profit = sell_price - buy_price
                res_profit = max(profit, res_profit)
                l += 1
        return res_profit



        