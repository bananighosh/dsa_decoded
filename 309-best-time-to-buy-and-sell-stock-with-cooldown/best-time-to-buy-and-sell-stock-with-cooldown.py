class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, sell):
            if i >= len(prices):
                return 0
            if sell:
                sold = dfs(i+2, not sell) + prices[i]
                unsold = dfs(i+1, sell)
                return max(sold, unsold)
            else:
                buy = dfs(i+1, not sell) - prices[i]
                unbuy = dfs(i+1, sell)
                return max(buy, unbuy)
        return dfs(0, False)
        
        