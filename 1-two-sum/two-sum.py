class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hset = {}

        for i, num in enumerate(nums):

            if (target - num) in hset:
                return [i, hset[target - num]]
            
            hset[num] = i
        
        return []
        