class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for direction, num_shifts in shift:
            num_shifts %= len(s)

            if( direction == 0 ):
                s = s[num_shifts:] + s[:num_shifts]
            else:
                s = s[-num_shifts:] + s[:-num_shifts]

        return s
