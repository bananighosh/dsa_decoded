class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Sol 3: for O(n) O(1)
        n = len(nums)
        res = [1] * n
        curr = 1

        for i in range(n):
            res[i] *= curr
            curr *= nums[i]
        
        curr = 1
        for i in range(n - 1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        
        return res


        # # Sol 2
        # n = len(nums)

        # pre = [0] * n
        # suffix = [0] * n

        # pre[0] = 1
        # suffix[n - 1] = 1

        # for i in range(1, n):
        #     pre[i] = pre[i - 1] * nums[i - 1]
        
        # for i in range(n - 2, -1, -1):
        #     suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # res = [0] * n
        # for i in range(n):
        #     res[i] = pre[i] * suffix[i]
        
        # return res
        