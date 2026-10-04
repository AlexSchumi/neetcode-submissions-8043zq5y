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



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # 1. Update lowest buy price seen so far
            if price < min_price:
                min_price = price
            # 2. Check profit if sold today
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
        