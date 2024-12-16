class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        curr_min, curr_i = nums[0], 0
        #heap ??
        res = nums

        pq = []

        for i, val in enumerate(nums):
            heappush(pq, (val, i))
        
        for i in range(k):
            curr_min, min_idx = heappop(pq)
            res[min_idx] *= multiplier
            heappush(pq, (res[min_idx], min_idx))

        return res
        # for i in range(k):
        #     for j, val in enumerate(nums):
        #         if curr_min == val:

        #         curr_min = min(curr_min, val)


        