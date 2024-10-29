class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        # dp = [0 for _ in range(n + 1)]
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        prev, curr = 1, 2

        for i in range(3, n+1):
            next = prev + curr
            prev = curr
            curr = next
        
        return curr
        
        return dp[n]