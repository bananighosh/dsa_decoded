class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using minheap we can solve this
        # insert all the array nums and the frequencies in the maxheap
        # pop top K elements
        # TC : O(nlogk)

        freq = Counter(nums)
        # https://pythontic.com/algorithms/heapq/nlargest
        return heapq.nlargest(k, freq.keys(), key = freq.get)
        