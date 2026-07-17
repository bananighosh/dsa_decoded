class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for curr_i, curr_temp in enumerate(temperatures):

            while stack and curr_temp >  stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = curr_i -  prev_idx
            
            stack.append([curr_temp, curr_i])
        
        return res

        