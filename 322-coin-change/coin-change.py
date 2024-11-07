class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}
        def dfs(i, curAmount):
            if (i, curAmount) in dp:
                return dp[(i,curAmount)]
            if i == len(coins) and curAmount == amount:
                return 0
            if curAmount > amount or i == len(coins):
                return float("inf")
            
            
            pick = 1+ dfs(i, curAmount + coins[i])
            npick = dfs(i+1, curAmount)

            dp[(i,curAmount)] = min(npick, pick)

            return dp[(i,curAmount)]

        ans = dfs(0, 0)

        return -1 if ans == float("inf") else ans
        