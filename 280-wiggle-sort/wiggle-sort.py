class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        nums.sort()
        for n in range(1, len(nums)-1, 2):
            nums[n], nums[n+1] = nums[n+1], nums[n]

        