class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
       

        # return self.dfs(0, -1, nums)
        return self.dp(0, nums)
    

    def dfs(self, idx, prev, nums):
        if idx == len(nums):
            return 0
        ar_seq = self.dfs(idx + 1, prev, nums)
        if prev == -1 or nums[idx] - prev == prev - nums[idx - 1]:
            ar_seq = 1 + self.dfs(idx + 1, nums[idx], nums)
        
        return ar_seq
       # didn't work at all:
        # dp = {}
        # if (idx, prev) in dp:
        #     return dp[(idx, prev)]
        # if idx == len(nums):
        #     dp[(idx, prev)] = 0
        # ar_seq = self.dfs(idx + 1, prev, nums)
        # if prev == -1 or nums[idx] - prev == prev - nums[idx - 1]:
        #     ar_seq = 1 + self.dfs(idx + 1, nums[idx], nums)
        # dp[(idx, prev)] = ar_seq
        # return dp[(idx, prev)]
    
    def dp(self, idx, nums):
        res = 0
        n = len(nums)

        # array with idx as key and hashmap as value store the no. of sq till the current idx & diff
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] +=  1 +  dp[j][diff]
                # res += dp[i][diff] #35 tc
                res  += dp[j][diff]
        
        # return res - (n * (n - 1) // 2)
        return res


