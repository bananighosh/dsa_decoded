class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = res = curr_len = 0

        for num in nums:
            if num > max_val:
                max_val = num
                res = curr_len = 0

            if num == max_val:
                curr_len += 1
            else:
                curr_len = 0

            res = max(res, curr_len) 
        
        return res
        