class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = set()

        for i in range(len(nums)):
            f = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = f + nums[left] + nums[right]
                if curr_sum == 0:
                    # return [f, nums[left], nums[right]]
                    res.add((f, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(res)
            

        