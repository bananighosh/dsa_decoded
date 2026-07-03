class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subseq_lens = defaultdict(list)

        for num in nums:
            if subseq_lens[num - 1]:
                prev_len = heapq.heappop(subseq_lens[num - 1])
                heapq.heappush(subseq_lens[num], prev_len + 1)
            else:
                heapq.heappush(subseq_lens[num], 1)
        
        for lengths in subseq_lens.values():
            for length in lengths:
                if length < 3:
                    return False

        return True
        

