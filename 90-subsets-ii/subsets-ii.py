class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res =[]

        def backtrack(i, subset):
            if (i == len(nums)):
                res.append(subset[::])
                return
            

            # include the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # not include the current element
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res

        