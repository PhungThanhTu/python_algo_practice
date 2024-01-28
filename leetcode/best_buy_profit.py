# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1157402653/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        maxPro = 0
        bestBuy = prices[0]
        for i in range(1, len(prices)):
            print(f'best buy {bestBuy} maxPro {maxPro}')
            if prices[i] < bestBuy:
                bestBuy = prices[i]
            if prices[i] > bestBuy:
                if maxPro < prices[i] - bestBuy:
                    maxPro = prices[i] - bestBuy
        return maxPro
    
print(Solution().maxProfit([7,1,5,3,6,4]))