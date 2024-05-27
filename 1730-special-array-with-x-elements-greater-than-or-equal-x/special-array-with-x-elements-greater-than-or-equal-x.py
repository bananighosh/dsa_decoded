class Solution:
    def specialArray(self, nums: List[int]) -> int:

        count = Counter(nums)
        print(count)

        count_so_far = 0

        for i in range(max(nums), -1, -1):
            count_so_far += count[i]

            if count_so_far == i:
                return i
        
        return -1