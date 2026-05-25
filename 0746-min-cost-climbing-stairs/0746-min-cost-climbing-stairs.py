class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        dp = [-1] * (n + 1)

        def solve(n):
            if n <= 1:
                return 0

            if dp[n] != -1:
                return dp[n]

            left = solve(n - 1) + cost[n - 1]
            right = solve(n - 2) + cost[n - 2]

            dp[n] = min(left, right)
            return dp[n]   

        return solve(n)     