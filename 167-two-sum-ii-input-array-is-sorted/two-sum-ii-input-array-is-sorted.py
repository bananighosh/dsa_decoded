class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Solution utilizing sorted - O(n) O(1)

        left = 0
        right = len(numbers) - 1

        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if  curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return []

        # # General solution - O(n) O(n)
        # s_map = {}

        # for i in range(len(numbers)):
        #     rem = target - numbers[i]

        #     if rem in s_map:
        #         return [s_map[rem] + 1, i + 1]

        #     s_map[numbers[i]] = i

        # return []     