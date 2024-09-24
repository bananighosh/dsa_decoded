class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        for ind,n in enumerate(nums[:-1]):
            if maxi == ind and n == 0:
                return False
            maxi = max(maxi, ind+n)
        return True

        