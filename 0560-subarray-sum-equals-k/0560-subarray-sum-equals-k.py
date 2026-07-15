class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        res = 0
        prefix_sum_so_far = 0

        for num in nums:
            prefix_sum_so_far += num
            res += freq[prefix_sum_so_far - k]
            freq[prefix_sum_so_far] += 1
        
        return res
        