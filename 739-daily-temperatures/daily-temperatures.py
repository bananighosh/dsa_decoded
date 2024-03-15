class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Sol 2 : monotonic decreasing stack
        res = [0] * len(temperatures)
        stack = [] # {temp, idx}

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            # else:
            stack.append([temp, idx])
        
        return res

            



        

        # Sol 1 : brute force O(n^2)
        # consider the curr_val and traverse from curr_idx + 1  to find the next higher temp
        # subtract the indices and store + 1 for num days to next high temp


        