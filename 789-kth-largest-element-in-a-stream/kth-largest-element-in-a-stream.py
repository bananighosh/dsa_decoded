class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        # will only keep the k lasrgest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #add new elememt to the minHeap
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # kth largest element - top of the heap
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)