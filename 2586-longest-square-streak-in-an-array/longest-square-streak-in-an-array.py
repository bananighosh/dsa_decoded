class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # sort the array
        # search the array for squares of each and update count - but O(n^2)
        # O(n) or <O(n^2) ??
        # sol1 : binary search
        
        # sol2: 
        nums.sort()
        visited = set(nums)
        longest_streak = 0

        print(nums)
        for num in nums:
            curr_streak = num
            curr_streak_len = 0

            while curr_streak in visited:
                curr_streak_len += 1
                curr_streak = curr_streak ** 2

            if curr_streak_len > 1:
                longest_streak = max(longest_streak, curr_streak_len)
            
        return longest_streak if longest_streak > 1 else -1
