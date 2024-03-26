class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Sol 2:
        res = []
        curr = []
        def backtrack(curr, nums):
            if not nums:
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                backtrack(curr +[nums[i]], nums[:i] + nums[i+1:])
        
        backtrack(curr, nums)
        return res

        # Sol 1:
        # res = []
        # curr = []

        # def backtrack(i):
        #     if i >= len(nums):
        #         res.append(nums.copy())
        #         return
            
        #     for j in range(i, len(nums)):

        #         nums[j], nums[i] = nums[i], nums[j]
        #         backtrack(i + 1)
        #         nums[j], nums[i] = nums[i], nums[j]
                
        
        # backtrack(0)
        # return res
        