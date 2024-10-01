class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        hashMap[0] = 1
        ans = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            ans += hashMap[prefixSum-k]
            hashMap[prefixSum] += 1
        return ans
        