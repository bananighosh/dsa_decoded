class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        freqMap = defaultdict(int)
        maxNum = -1

        for n in nums:
            freqMap[n] += 1
        
        for key, val in freqMap.items():
            if val == 1:
                maxNum = max(maxNum, key)
        
        return maxNum


        