class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sol1
        # heap consists of the distance from origin and the point list, 
        # sorted on the basis of distance

        # minHeap = []
        # res = []

        # for curr in points:

        #     dist = curr[0] ** 2 + curr[1] ** 2
        #     minHeap.append([dist, curr])
        
        # print(minHeap)
        # heapq.heapify(minHeap)
        # print(minHeap)

        # while k != 0:
        #     dist, point = heapq.heappop(minHeap)
        #     res.append(point)
        #     k -= 1
        
        # return res 


        # #sol2 - fastest
        # if k == len(points):
        #     return points

        # points = sorted(points, key = lambda x: x[0] ** 2 + x[1] ** 2)
        # return points[:k]

        #sol3 maxHeap
        maxHeap = []

        size = 0

        for curr in points:
            dist = curr[0] ** 2 + curr[1] ** 2
            heapq.heappush(maxHeap, (-1*dist, curr))
            size += 1

            if size > k:
                heapq.heappop(maxHeap)
                size -= 1
            
        res = [i[1] for i in maxHeap]
        return res