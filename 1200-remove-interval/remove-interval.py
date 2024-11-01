class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        rem_start, rem_end = toBeRemoved
        res = []

        print(rem_start, rem_end )

        for start, end in intervals:
            if start > rem_end or end < rem_start:
                res.append([start, end])
            else:
                if start < rem_start:
                    res.append([start, rem_start])
                if end > rem_end:
                    res.append([rem_end, end])
        
        return res



        