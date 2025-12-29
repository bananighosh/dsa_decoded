class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        freq = Counter(nums)

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        while len(res) < k:
            curr = heapq.heappop(heap)
            res.append(curr[1])
        
        return res
        