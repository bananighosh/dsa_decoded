class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort on basis of start key
        intervals.sort(key = lambda i : i[0])

        res = []

        for interval in intervals:
            # if curr start is greater or beyond the last End
            if not res or interval[0] >  res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res
        