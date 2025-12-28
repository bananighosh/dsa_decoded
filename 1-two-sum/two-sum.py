class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        container = defaultdict(int)

        for i, num in enumerate(nums):
            curr = target - num
            if curr in container:
                return [container[curr], i]
            
            container[num] = i
        
        return []
        