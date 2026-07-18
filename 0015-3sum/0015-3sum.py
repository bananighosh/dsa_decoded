class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low, high = i + 1, n - 1
            while low < high:
                currSum = num + nums[low] + nums[high]
                if currSum == 0:
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1 

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif currSum < 0:
                    low += 1
                else:
                    high -= 1
        
        return res

        