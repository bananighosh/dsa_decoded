class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ## Sol 2:
        nums.sort()
        count = 0

        for x in range(len(nums) + 1):
            count = sum(1 for num in nums if num >= x)
            print(count, x)

            if count == x:
                return x
        return -1

        ## Sol 1: 
        # count = Counter(nums)
        # print(count)

        # count_so_far = 0

        # for i in range(max(nums), -1, -1):
        #     count_so_far += count[i]

        #     if count_so_far == i:
        #         return i
        
        # return -1