class Solution:
    def maxProfit(self, prices) -> int:
        profit,max_profit = 0,0
        i,j = 0,1
        while j < len(prices):
            if prices[j] - prices[i] <= 0:
                i = j
                j += 1
            elif prices[j] - prices[i] > 0:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                j += 1
        return max_profit