class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for item in shift:
            direction = item[0]
            num_shifts = item[1]
            num_shifts %= len(s)
          
            print(num_shifts, s[-num_shifts:], s[:-num_shifts])
            if( direction == 0 ):
                s = s[num_shifts:] + s[:num_shifts]
            else:
                s = s[-num_shifts:] + s[:-num_shifts]

        return s
