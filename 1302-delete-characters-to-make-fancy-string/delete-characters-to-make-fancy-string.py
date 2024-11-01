class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []

        left = 0
        res.append(s[left])
        
        for right in range(1, len(s)):

            res.append(s[right])
            # print(s[left], s[right], res)
            
            if s[left] == s[right]:
                if right - left + 1 > 2:
                    res.pop()
                    # left += 1
            else:
                left = right
            # print(s[left], s[right], left, right)
        
        return ''.join(res)
