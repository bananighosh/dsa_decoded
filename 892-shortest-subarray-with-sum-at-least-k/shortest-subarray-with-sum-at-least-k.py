class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Compute prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Deque to store indices of the prefix sums
        dq = deque()
        min_len = float('inf')
    
        for i in range(n + 1):
            # Check if the current  subarray satisfies the condition
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            
            # Maintain the deque in increasing order of prefix sums
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        # left = window_sum = 0
        # min_len = float('inf')

        # for right in range(len(nums)):
        #     window_sum += nums[right]

        #     print(window_sum, k)

        #     while window_sum >= k:
        #         min_len = min(min_len, right - left + 1)
        #         window_sum -= nums[left]
        #         left += 1
            
        return min_len if min_len != float('inf') else -1
   