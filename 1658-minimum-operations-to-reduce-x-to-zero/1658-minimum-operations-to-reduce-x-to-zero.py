class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 1:
            return -1

        left = 0
        windowSum = 0
        maxLen = float("-inf")

        for right, num in enumerate(nums):
            windowSum += num

            while windowSum > target:
                windowSum -= nums[left]
                left += 1
            
            if windowSum == target:
                maxLen = max(maxLen, right - left + 1)
        
        return len(nums) - maxLen if not math.isinf(maxLen) else -1