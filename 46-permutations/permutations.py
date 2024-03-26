class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i):
            if i >= len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, len(nums)):

                nums[j], nums[i] = nums[i], nums[j]
                backtrack(i + 1)
                nums[j], nums[i] = nums[i], nums[j]
                
        
        backtrack(0)
        return res
        