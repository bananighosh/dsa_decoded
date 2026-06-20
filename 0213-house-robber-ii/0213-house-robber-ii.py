class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_circular(nums):
            n = len(nums)
            dp = [-1] * n
            def traverse(i):
                if i < 0: return 0
                if i == 0:
                    return nums[i]
                if dp[i] != -1:
                    return dp[i]
                pick = nums[i] + traverse(i - 2)
                n_pick = traverse(i - 1)
                dp[i] = max(pick, n_pick)
                return dp[i]
            return traverse(n - 1)
        
        return max(rob_circular(nums[:-1]), rob_circular(nums[1:]) )


        