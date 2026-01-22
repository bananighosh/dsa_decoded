class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        ops = 0

        def is_non_decreasing(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return True
            return False
        
        while is_non_decreasing(nums):
            minSum = nums[0] + nums[1]
            idx = 0

            for i in range(1, len(nums) - 1):
                currSum = nums[i] + nums[i + 1]
                if currSum < minSum:
                    minSum = currSum
                    idx = i
            
            nums[idx] = minSum
            nums.pop(idx + 1)
            ops += 1
        
        return ops