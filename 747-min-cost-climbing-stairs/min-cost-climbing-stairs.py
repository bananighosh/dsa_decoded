class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        ## sol 1
        # @cache
        # def minCost(n):
        #     if n == 0:
        #         return cost[0]
        
        #     if n == 1:
        #         return cost[1]
        
        #     return cost[n] + min(minCost(n - 1), minCost(n - 2))

        ## sol 2
        # def minCostDP(n):
        #     if dp[n] != -1:
        #         return dp[n]
        #     if n <= 1:
        #         dp[n] = cost[n]
        #     else:
        #         dp[n] = cost[n] + min(minCostDP(n - 1), minCostDP(n - 2))
            
        #     return dp[n]

        # n = len(cost)
        # dp = [-1] * n
        # return min(minCostDP(n - 1), minCostDP(n - 2))

        ## sol 3
        n = len(cost)

        if n == 1:
            return cost[0]

        prev , curr = cost[0], cost[1]
               
        for i in range(2, n):
            next = cost[i] + min(prev, curr)
            prev = curr
            curr = next
        
        return min(prev, curr)
 
        