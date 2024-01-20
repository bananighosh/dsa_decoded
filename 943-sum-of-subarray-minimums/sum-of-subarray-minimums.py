class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # find all subarrays
        # store minimum in the subarray in an array
        # add all the stored values to return the min sum
        # didn't work

        #sol
        mod = 10**9 + 7
        stack = []
        result = 0

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result = (result + arr[j] * (i - j) * (j - k)) % mod

            stack.append(i)

        # Handle remaining elements in the stack
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            result = (result + arr[j] * (len(arr) - j) * (j - k)) % mod

        return result