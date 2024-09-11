class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        last = -1
        start = 0
        for end, i in enumerate(nums):
            if i == 0:
                if last == -1:
                    last = end
                    ans = max(ans, end-start+1)
                else:
                    start = last + 1
                    last = end
            ans = max(ans, end-start+1)
        return ans
        