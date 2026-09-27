class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy = float("inf")
        maxProfit = 0

        for price in prices:
            buy = min(buy, price)
            maxProfit = max(maxProfit, price - buy)
        
        return maxProfit