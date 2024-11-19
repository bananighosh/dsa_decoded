class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        left = right = 0
        max_sum = 0
        curr_sum = 0
        start_idx = end_idx = 0
        dist_window = set()

        while right < len(nums):
            curr_sum += nums[right]
            
            while right - left + 1 > k or nums[right] in dist_window:
                curr_sum -= nums[left]
                dist_window.remove(nums[left])
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                start_idx = left
                end_idx = right
            
            dist_window.add(nums[right])
            right += 1
        
        return max_sum

        