class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heap implementation - minheap with (-) sign for elem freq
        heap = []
        freq = Counter(nums)
        
        for num,count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        print(heap)
        res = []
        while len(res) < k:
            curr = heapq.heappop(heap)
            res.append(curr[1])
        
        return res
        