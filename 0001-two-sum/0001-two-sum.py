class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)

        for i, num in enumerate(nums):
            curr = target - num
            if curr in hmap:
                return [i, hmap[curr]]
            
            hmap[num] = i
        
        return []
        