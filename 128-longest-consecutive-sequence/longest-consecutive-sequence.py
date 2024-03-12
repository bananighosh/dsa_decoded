class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution 1:
        # Sort the array and check length until the curr_num is +1 of prev num
        # check the curr _len and update max_len 
        # check the curr number - 1 if exists, else it starts the sequence
        # check if the next number, i.e., curr_num + 1 in the set or not

        seq = set(nums)
        res = []
        max_len = 0

        for num in nums:
            if (num - 1) not in seq:
                curr_len = 0
                while (num + curr_len) in seq:
                    curr_len += 1
                max_len = max(curr_len, max_len)
        
        return max_len

        