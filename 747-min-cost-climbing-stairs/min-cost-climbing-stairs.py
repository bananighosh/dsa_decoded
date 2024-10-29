class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def minCost(n):
            if n == 0:
                return cost[0]
        
            if n == 1:
                return cost[1]
        
            return cost[n] + min(minCost(n - 1), minCost(n - 2))
        
        n = len(cost)
        return min(minCost(n - 1), minCost(n - 2))

        