class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # m={}
        # for i in range(0,len(numbers)):
        #     if target-numbers[i] in m :
        #         return [m[target-numbers[i]]+1,i+1]
        #     m[numbers[i]]=i
        # return []

        s_map = {}

        for i in range(len(numbers)):
            rem = target - numbers[i]

            if rem in s_map:
                return [s_map[rem] + 1, i + 1]

            s_map[numbers[i]] = i

        return []     