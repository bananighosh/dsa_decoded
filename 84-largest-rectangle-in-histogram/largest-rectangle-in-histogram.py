class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # {index, height}
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop() # pop the larger height as it cannot be extended forward
                maxArea = max(maxArea, height * (i - idx)) 
                start = idx #traverse backwards
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) 

        return maxArea  

        