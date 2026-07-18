class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        hmap = {0: -1}

        for i, num in enumerate(nums):
            prefixSum += num
            prefixSumMod = prefixSum % k

            if prefixSumMod in hmap:
                if i - hmap[prefixSumMod] > 1:
                    return True
            else:
                hmap[prefixSumMod] = i
        
        return False
        