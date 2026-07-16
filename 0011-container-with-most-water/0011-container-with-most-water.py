class Solution:
    def maxArea(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1
        maxArea = 0

        while i < j:

            h = min(height[i], height[j])
            w = j - i

            maxArea = max(maxArea, w * h)
            print(maxArea)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea 

        