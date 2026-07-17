class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        maxProfit = 0

        while r < n:
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
            else:
                l = r
            r += 1
        
        return maxProfit


        