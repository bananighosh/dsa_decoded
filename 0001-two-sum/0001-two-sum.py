class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict()

        for i,num in enumerate(nums):
            curr = target - num
            if curr in hmap:
                return [hmap[curr], i]

            hmap[num] = i
        
        return []
        