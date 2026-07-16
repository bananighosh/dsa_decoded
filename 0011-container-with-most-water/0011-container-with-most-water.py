class Solution:
    def maxArea(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1
        maxArea = 0

        while i < j:
            l_height, r_height = height[i], height[j]
            h = min(l_height, r_height)
            w = j - i

            maxArea = max(maxArea, w * h)

            if l_height < r_height:
                while i < j and l_height >= height[i] :
                    i += 1
            else:
                while i < j  and r_height >= height[j]:
                    j -= 1
               

        return maxArea 

        