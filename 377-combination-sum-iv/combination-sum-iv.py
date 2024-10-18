class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):
            if total == target:
                return 1
            if total > target:
                return 0
            count = 0

            for num in nums:
                count += dfs(i+1, num+total)
            return count
        return dfs(0,0)
        