class Solution:
    def findMin(self, nums: List[int]) -> int:

        res_idx = 0
        l, r = 0, len(nums) - 1

        while l <= r:

            while l < r and nums[l] == nums[l + 1]: l = l + 1
            while r > l and nums[r] == nums[r - 1]: r = r - 1

            mid = l + (r - l) // 2

            if nums[mid] < nums[res_idx]:
                res_idx = mid
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            
        return nums[res_idx]
        