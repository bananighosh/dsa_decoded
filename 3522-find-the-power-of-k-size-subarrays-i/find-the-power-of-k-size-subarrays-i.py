class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = [-1] * (len(nums) - k + 1)


        for right in range(len(nums)):
            if nums[right] - nums[right - 1] != 1:
                left = right

            while right - left + 1 > k: # or nums[right] != right - left + 1:
                left += 1
            
            if right - left + 1 == k:
                res[right - k + 1] = nums[right]
        
        return res

        