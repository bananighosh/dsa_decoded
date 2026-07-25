class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0
        dp = [-1] * (n + 1)

        def rob(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            if i == 0:
                dp[i] = nums[i]

            pick = nums[i] + rob(i - 2) 
            n_pick = rob(i - 1)

            dp[i] = max(pick, n_pick)
            return dp[i]
        
        return rob(n - 1)
        