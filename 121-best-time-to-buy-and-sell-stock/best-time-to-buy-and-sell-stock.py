class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Sol 2: Kadane's algo (DP technique) - modified
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i] # find the lowest buy
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        
        return profit

        # # Sol 1
        # left = 0 
        # right = left + 1
        # maxProfit = 0

        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         maxProfit = max(maxProfit, prices[right] - prices[left])
        #     else:
        #         left = right # skip to the next lowest

        #     right += 1
        
        # return maxProfit
            