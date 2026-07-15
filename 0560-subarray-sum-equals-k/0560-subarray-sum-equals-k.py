class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        prefixSum = 0

        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefixSum += num
            res += freq[prefixSum - k]
            freq[prefixSum] += 1
        
        return res
        