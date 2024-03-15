class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Sol 3 :  O(n) O(1)
        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 2, -1, -1):
            top = i + 1
            while top < n and temperatures[i] >= temperatures[top]:
                if ans[top] == 0:
                    top = n  # top = n means there is no found
                    break
                top = ans[top] + top
            if top < n:
                ans[i] = top - i
        return ans

        # Sol 2 : monotonic decreasing stack - O(n) O(n)
        # res = [0] * len(temperatures)
        # stack = [] # {temp, idx}

        # for idx, temp in enumerate(temperatures):
        #     while stack and  temp > stack[-1][0]:
        #         prev_temp, prev_idx = stack.pop()
        #         res[prev_idx] = idx - prev_idx
        #     # else:
        #     stack.append([temp, idx])
        
        # return res

        # Sol 1 : brute force O(n^2)
        # consider the curr_val and traverse from curr_idx + 1  to find the next higher temp
        # subtract the indices and store + 1 for num days to next high temp


        