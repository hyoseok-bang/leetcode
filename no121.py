# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = sys.maxsize
        
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        
        return profit
