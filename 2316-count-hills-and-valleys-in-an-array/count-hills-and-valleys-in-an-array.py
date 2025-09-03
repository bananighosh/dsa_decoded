class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0

        for j in range(1, len(nums) - 1):
            if nums[j] != nums[j + 1]:
                if nums[j] > nums[i] and nums[j] > nums[j + 1] or \
                    nums[j] < nums[i] and nums[j] < nums[j + 1]:
                        res += 1
                i = j
                 
        return res
            
        