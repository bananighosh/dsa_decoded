class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum = 0
        res = 0
        hmap = defaultdict(int)
        hmap[0] = 1

        for num in nums:
            prefixSum += num
            res += hmap[prefixSum - k]
            hmap[prefixSum] += 1
        
        return res
        