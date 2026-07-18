class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 1:
            return -1

        hmap = {0:-1}
        prefixSum = 0
        maxLen = float("-inf")

        for i, num in enumerate(nums):
            prefixSum += num

            if prefixSum - target in hmap:
                maxLen = max(maxLen, i - hmap[prefixSum - target])
            hmap[prefixSum] = i
        
        print(math.isinf(maxLen))
        
        return len(nums) - maxLen if not math.isinf(maxLen) else -1