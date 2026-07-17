class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = float("inf")
        maxProfit = 0

        for price in prices:
            buy = min(buy, price)
            currProfit = price - buy
            maxProfit = max(maxProfit, currProfit)

        return maxProfit


        