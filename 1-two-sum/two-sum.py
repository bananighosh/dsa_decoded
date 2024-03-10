class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        t_map = defaultdict(int)
        n = len(nums)

        for i in range(n):
            num = target - nums[i]

            if num in t_map:
                return [t_map[num], i]
            
            t_map[nums[i]] = i
        
        return []
        