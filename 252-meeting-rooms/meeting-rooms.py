class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if not intervals:
            return True

        intervals.sort()
        prev_end =  intervals[0][1]
        for curr_interval in intervals[1:]:
            if curr_interval[0] >= prev_end:
                prev_end = curr_interval[1]
                continue
            else:
                return False
        
        return True
        