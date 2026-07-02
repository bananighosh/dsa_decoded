class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        largest = None
        
        # freq = Counter(nums)

        # for num,count in freq.items():
        #     heapq.heappush(heap, -num)
        
        for num in nums:
            heapq.heappush(heap, -num)
        
        while k > 0:
            largest = -heapq.heappop(heap)
            k = k - 1
        
        return largest