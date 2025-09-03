class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        n = len(nums)

        for j in range(1, n - 1):
            if nums[j] > nums[i] and nums[j] > nums[j + 1]:
                res += 1 #hill
                i = j
            elif nums[j] < nums[i] and nums[j] < nums[j + 1]:
                res += 1 # valley
                i = j
            while j < n - 1 and nums[j] == nums[j + 1]:
                j += 1
        
        return res
            
        