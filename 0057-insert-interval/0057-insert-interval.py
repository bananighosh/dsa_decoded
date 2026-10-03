class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        res = []

        for interval in intervals:
            start, end = interval[0], interval[1]

            if end < newInterval[0]:
               res.append(interval)
            
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start,end]

            else:
                start = min(start, newInterval[0] )
                end = max(end, newInterval[1])
                newInterval = [start,end]
            
        res.append(newInterval)
        return res
        