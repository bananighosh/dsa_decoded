class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        nums.sort()
        res = set()
        for i, num in enumerate(nums):
            low, high = i + 1, n - 1
            while low < high:
                currSum = num + nums[low] + nums[high]
                if currSum == 0:
                    res.add((num, nums[low], nums[high]))
                    low += 1
                    high -= 1

                elif currSum < 0:
                    low += 1
                else:
                    high -= 1
        
        return list(res)

        