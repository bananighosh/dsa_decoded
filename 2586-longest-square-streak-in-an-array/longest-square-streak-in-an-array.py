class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        #sort the array
        # search the array for squares of each and update count - but O(n^2)
        # O(n) or <O(n^2) ??

        nums.sort()
        visited = set()

        longest_streak = 0

        def binary_search(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for num in nums:
            if num in visited:
                continue
            
            curr_streak = num
            # sq_curr_streak = num * num
            curr_streak_len = 1
            
            while curr_streak * curr_streak <= 10**5:
                if binary_search(nums, curr_streak * curr_streak):
                    curr_streak *= curr_streak
                    visited.add(curr_streak)
                    curr_streak_len += 1
                else:
                    break
            
            longest_streak = max(longest_streak, curr_streak_len)
        
        return longest_streak if longest_streak >= 2 else -1
