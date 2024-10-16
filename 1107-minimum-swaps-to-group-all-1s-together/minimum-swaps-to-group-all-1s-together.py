class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount = 0
        for value in data:
            if value == 1: 
                oneCount += 1
        window = oneCount
        maxCount = 0
        for i in range(window):
            if data[i] == 1:
                maxCount += 1
        left = 0
        globalMax = maxCount
        for value in data[window:]:
            if value == 1:
                maxCount += 1
            if data[left] == 1:
                maxCount -= 1
            left += 1
            globalMax = max(maxCount, globalMax)
        

        return window-globalMax
            


        