class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            plus = dfs(i+1, curr + nums[i])
            minus = dfs(i+1, curr - nums[i])
            return plus + minus
        
        return dfs(0, 0)
        