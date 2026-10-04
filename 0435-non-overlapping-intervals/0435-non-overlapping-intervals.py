class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0
        i, j = 0,  1
        n = len(intervals)

        while j in range(n):
            if intervals[i][1] <= intervals[j][0]:  # non-overlapping
                i = j
                j += 1
            elif intervals[i][1] <= intervals[j][1]:
                j += 1
                res += 1
            elif intervals[i][1] > intervals[j][1]:
                i = j
                j += 1
                res += 1
        return res
                




