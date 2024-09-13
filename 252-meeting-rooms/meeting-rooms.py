class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                return False
            end = interval[1]
        return True
        