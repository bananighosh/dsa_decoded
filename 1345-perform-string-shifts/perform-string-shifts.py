class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        for item in shift:
            direction = item[0]
            amount = item[1] % len(s)

            if direction == 0:
                s = s[amount:] + s[:amount]
            else:
                s = s[-amount:] + s[:-amount]
        
        return s
        
        