class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        s_map = {}

        for i in range(len(numbers)):
            rem = target - numbers[i]

            if rem in s_map:
                return [s_map[rem] + 1, i + 1]

            s_map[numbers[i]] = i

        return []     