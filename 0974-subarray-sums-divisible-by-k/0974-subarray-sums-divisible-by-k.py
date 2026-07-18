class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefixSum = 0
        res = 0

        hmap = defaultdict(int)
        hmap[0] = 1

        for i, num in enumerate(nums):
            prefixSum += num
            prefixSumMod = prefixSum % k
            res += hmap[prefixSumMod]
            
            hmap[prefixSumMod] += 1
        
        return res
            



        