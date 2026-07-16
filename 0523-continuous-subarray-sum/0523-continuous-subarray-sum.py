class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefixSumMod = 0
        prefixSumModFreq = {0: -1}

        for i, num in enumerate(nums):
            prefixSumMod = (prefixSumMod + nums[i]) % k

            if prefixSumMod in prefixSumModFreq:
                if i - prefixSumModFreq[prefixSumMod] > 1:    
                    return True
            else:
                prefixSumModFreq[prefixSumMod] = i
        return False

        