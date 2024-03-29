class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxLeft = []
        # maxRight = []

        # minLeftRight = []

        left, right = 0 , len(height) - 1
        maxArea = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

# TC: O(n) O(1)

            

        
        
        