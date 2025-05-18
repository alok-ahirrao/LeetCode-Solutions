from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,l=1,0
        maxProfit = 0
        while r<len(prices):
            profit=0
            if prices[l] <prices[r]:
                profit = prices[r] -prices[l]
            else:
                l=r
            maxProfit=max(maxProfit,profit)
            r+=1
        return maxProfit
            

