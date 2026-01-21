class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n != 2:
                res.append(n - ((n + 1) & (-n - 1)) // 2)
            else:
                res.append(-1)
        return res
        