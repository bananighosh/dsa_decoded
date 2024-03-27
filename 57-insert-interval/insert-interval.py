class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals:
        #     return [newInterval]

        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append(intervals[i])
            else:
                new_start = min(intervals[i][0], newInterval[0])
                new_end = max(intervals[i][1], newInterval[1])
                newInterval = [new_start, new_end]
        
        res.append(newInterval)
        
        return res

        