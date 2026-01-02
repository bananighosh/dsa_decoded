class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        def euclidDist(x, y):
            d = x**2 + y**2
            return math.sqrt(d)
        
        for point in points:
            dist = euclidDist(point[0], point[1])
            heapq.heappush(heap, (dist, point))
        
        while len(res) < k:
            curr = heapq.heappop(heap)
            res.append(curr[1])
        
        return res
        