class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        maxNum = -1
        uniqueNumFreqMap = defaultdict(int)

        for num in nums:
            uniqueNumFreqMap[num] += 1
        
        for key, value in uniqueNumFreqMap.items():
            if value == 1:
                maxNum = max(maxNum , key)

        return maxNum


        