class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        
    def balance(self, heap1, heap2):
        while len(heap1) - len(heap2) > 1:
            heapq.heappush(heap2, -1*heapq.heappop(heap1))
        while len(heap2) - len(heap1) > 1:
            heapq.heappush(heap1, -1 *heapq.heappop(heap2))
        return
    def addNum(self, num: int) -> None:
        if not self.heap1 and not self.heap2:
            heapq.heappush(self.heap1, -1*num)
        elif num < -1 * self.heap1[0]:
            heapq.heappush(self.heap1, -1 * num)
            self.balance(self.heap1, self.heap2)
        else:
            heapq.heappush(self.heap2, num)
            self.balance(self.heap1, self.heap2)

        
        

    def findMedian(self) -> float:
        
        if len(self.heap1) == len(self.heap2):
            return (self.heap1[0] * -1 + self.heap2[0]) / 2
        elif len(self.heap1)> len(self.heap2):
            return -1 * self.heap1[0]
        else:
            return self.heap2[0] 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()