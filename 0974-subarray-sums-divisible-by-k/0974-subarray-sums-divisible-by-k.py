class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        res = 0

        hmap = defaultdict(int)
        hmap[0] = 1

        for num in nums:
            prefixSum += num
            prefixSumMod = prefixSum % k
            res += hmap[prefixSumMod]
            hmap[prefixSumMod] += 1
        
        return res
            



        