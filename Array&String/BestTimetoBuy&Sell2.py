# 122. Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        total_profit = 0
        buy, sell = 0, 0

        while sell < n:
            if prices[buy] < prices[sell]:
                total_profit += prices[sell] - prices[buy]
            buy = sell
            sell += 1

        return total_profit
    