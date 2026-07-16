class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefixSumMod = 0
        prefixSumModFreq = {0: -1}

        for i in range(n):
            prefixSumMod = (prefixSumMod + nums[i]) % k

            if prefixSumMod in prefixSumModFreq:
                if i - prefixSumModFreq[prefixSumMod] > 1:    
                    return True
            else:
                prefixSumModFreq[prefixSumMod] = i
        return False

        