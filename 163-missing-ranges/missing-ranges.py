class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        n = len(nums)

        if n == 0:
            res.append([lower, upper])
            return res

        # if x > lower and x < upper and not in nums:

        if nums[0] > lower:
            res.append([lower, nums[0] - 1])


        for idx in range(n - 1):
            if nums[idx + 1] - nums[idx] <= 1:
                continue
            res.append([nums[idx] + 1, nums[idx + 1] - 1])

        print(res)
        if nums[n - 1] < upper:
            res.append([nums[n-1] + 1 , upper])

        return res

        