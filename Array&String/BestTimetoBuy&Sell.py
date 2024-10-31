# 121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        buy_day, sell_day = 0, 0
        while buy_day < n - 1 and sell_day < n:
            profit = prices[sell_day] - prices[buy_day]
            if profit < 0:
                buy_day = sell_day
            elif profit > max_profit:
                max_profit = profit
            sell_day += 1
        return max_profit