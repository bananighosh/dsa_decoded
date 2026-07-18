class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, sell):
            if (i, sell) in dp:
                return dp[(i, sell)]
            if i >= len(prices):
                return 0
            if sell:
                sold = prices[i] + dfs(i + 2, not sell)
                unsold = dfs(i + 1, sell)
                dp[(i,sell)] = max(sold, unsold)
            else:
                buy = dfs(i + 1, not sell) - prices[i]
                unbuy = dfs(i + 1, sell)
                dp[(i,sell)] = max(buy, unbuy)
            
            return dp[(i,sell)]

        return dfs(0, False)
        