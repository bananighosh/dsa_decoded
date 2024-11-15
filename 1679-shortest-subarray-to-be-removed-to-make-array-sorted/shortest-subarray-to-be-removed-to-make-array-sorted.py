class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        res = right

        while left < right:

            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            res = min(res, right - left - 1)

            if arr[left] > arr[left + 1]:
                break
            
            left += 1
        
        return res
        
        return res