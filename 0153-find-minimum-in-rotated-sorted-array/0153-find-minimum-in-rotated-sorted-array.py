class Solution:
    def findMin(self, nums: List[int]) -> int:

        res_idx = 0
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] < nums[res_idx]:
                res_idx = mid
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return nums[res_idx]
        