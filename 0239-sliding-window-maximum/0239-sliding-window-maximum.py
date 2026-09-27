class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        heap = []
        i = 0
        j = 0
        n  = len(nums)

        while j < n:
            heapq.heappush(heap, (-nums[j], j))

            while heap and heap[0][1] < i:
                heapq.heappop(heap)

            if j - i + 1 == k:
                mx = -heap[0][0]
                res.append(mx)
                i += 1
            
            j += 1
        return res
        