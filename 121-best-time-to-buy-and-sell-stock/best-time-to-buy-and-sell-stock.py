class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0 
        right = left + 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right # skip to the next lowest

            right += 1
        
        return maxProfit
            