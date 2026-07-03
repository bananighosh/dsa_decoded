class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        subseq_lens = defaultdict(list)

        nums.sort()

        for num in nums:
            if subseq_lens[num - 1]:
                prev_len = heapq.heappop(subseq_lens[num - 1])
                if prev_len + 1 < k:
                    heapq.heappush(subseq_lens[num], prev_len + 1)
            else:
                heapq.heappush(subseq_lens[num], 1)

        for lengths in subseq_lens.values():
            for length in lengths:
                if length != k:
                    return False
        
        return True

