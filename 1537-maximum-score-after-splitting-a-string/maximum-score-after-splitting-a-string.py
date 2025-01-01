class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones =  s.count('1')
        zeros = max_score = 0

        for i in range(n - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            
            max_score = max(max_score, zeros + ones)
        
        return max_score
        