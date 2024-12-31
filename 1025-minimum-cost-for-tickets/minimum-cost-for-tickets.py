class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        left7 = left30 = 0

        dp = [0] * n

        for right in range(n):
            while days[right] - days[left7] >= 7:
                left7 += 1
            while days[right] - days[left30] >= 30:
                left30 += 1
            
            cost1 = dp[right - 1] + costs[0]
            cost7 = dp[left7 - 1] + costs[1]
            cost30 = dp[left30 - 1] + costs[2]

            dp[right] = min(cost1, cost7, cost30)
        
        return dp[n - 1]
        