class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        start = 0
        curr = 0
        for i, num in enumerate(nums):
            curr += num

            while curr >= target:
                ans = min(ans, i-start+1)
                curr -= nums[start]
                start += 1
                
        return ans if ans != float("inf") else 0
        