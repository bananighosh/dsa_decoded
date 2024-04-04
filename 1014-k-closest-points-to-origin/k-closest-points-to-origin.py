class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # heap consists of the distance from origin and the point list, 
        # sorted on the basis of distance

        minHeap = []
        res = []

        for curr in points:

            dist = curr[0] ** 2 + curr[1] ** 2
            minHeap.append([dist, curr])
        
        print(minHeap)
        heapq.heapify(minHeap)
        print(minHeap)

        while k != 0:
            dist, point = heapq.heappop(minHeap)
            res.append(point)
            k -= 1
        
        return res
         