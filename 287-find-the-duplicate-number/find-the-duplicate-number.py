class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # using xor we can do it
        # res = 0
        # for num in nums:
        #     res ^= num

        # for i in range(1, len(nums)):
        #     res ^= i
        
        # return res

        i = 0

        while True:
            i = int(abs(nums[i]))
            if nums[i] < 0:
                return i
            
            nums[i] = -1 * nums[i]
        



        