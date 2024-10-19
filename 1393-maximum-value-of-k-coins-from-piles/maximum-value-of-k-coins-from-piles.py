class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @cache
        def dfs(i, coins):
            if i == n:
                return 0
            res = dfs(i+1, coins)
            curPile = 0
            for j in range(min(coins, len(piles[i]))):
                curPile += piles[i][j]
                res = max(res, curPile + dfs(i+1, coins-j-1))
            return res
        
        return dfs(0, k)
        