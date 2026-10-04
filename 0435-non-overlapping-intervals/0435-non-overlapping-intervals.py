class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda i : i[ 1])
        non_overlap = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start >= prev_end:
                non_overlap += 1
                prev_end = end
        
        return len(intervals) - non_overlap

