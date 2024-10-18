class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(i, total):
            if total > amount:
                return 0
            if total == amount:
                return 1
            if i == n:
                return 0
            pick = dfs(i, total+coins[i])
            npick = dfs(i+1, total)
            return pick + npick
        return dfs(0, 0)