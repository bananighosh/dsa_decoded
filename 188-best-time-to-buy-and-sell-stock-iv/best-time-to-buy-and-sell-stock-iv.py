class Solution:
    def maxProfit(self, k:int, prices: List[int]) -> int:
        @cache
        def dfs(i, sell, count):
            if i >= len(prices):
                return 0
            if count == 2*k:
                return 0
            if sell:
                sold = dfs(i+1, not sell, count+1) + prices[i]
                unsold = dfs(i+1, sell, count)
                return max(sold, unsold)
            else:
                buy = dfs(i+1, not sell, count+1) - prices[i]
                unbuy = dfs(i+1, sell, count)
                return max(buy, unbuy)
        return dfs(0, False, 0)
        