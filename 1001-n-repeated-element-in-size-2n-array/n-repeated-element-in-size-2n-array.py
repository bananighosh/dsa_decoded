class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1] or (i+2 < n and nums[i] == nums[i + 2]):
                return nums[i]
        
        return nums[0]

        # explanation:  
        # given that the num is repeated "n" times
        # so majority element concept will cover exactly half of the array
        # if we pick min possible odd-length subarray of size 3
        # one of the elements should be duplicate
        # edge case : in case of 4 elements and duplicate element appears at
        # the ends so if duplicate not found we return the 1st element
        # as it is guaranteed one elem in the array is repeated so this edge works