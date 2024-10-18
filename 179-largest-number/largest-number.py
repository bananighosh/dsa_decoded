class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if not any(nums):
            return "0"

        class LargerStrComparator(str):
            def __lt__(self, other):
                return self + other > other + self

        heap = []
        for num in nums:
            heapq.heappush(heap, LargerStrComparator(str(num)))

        result = []
        while heap:
            result.append(heapq.heappop(heap))
        largest_num = "".join(result)
        return "0" if largest_num[0] == "0" else largest_num