class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_robbery = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            # either robs the house or doesn't rob the house
            # if robs , then robs both current and prev or prev as not adjacent
            # if doesn't rob, then robs just the previous
            max_robbery.append(max(nums[i] + max_robbery[i - 2], max_robbery[i - 1]))
        
        return max_robbery[len(nums) - 1]
        