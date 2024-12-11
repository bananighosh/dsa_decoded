class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 0
        left = 0

        for right in range(len(nums)):
            diff = nums[right] - nums[left]
            while diff > 2 * k:
                left += 1
                diff = nums[right] - nums[left]

            res = max(res, right - left + 1)
        
        return res
        