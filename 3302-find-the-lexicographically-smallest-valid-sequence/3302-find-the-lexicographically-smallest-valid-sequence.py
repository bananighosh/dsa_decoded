class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)

        rightMatched = 0
        rightMatchedCharLen = [0] * m
        i, j = m - 1, n - 1

        while i >= 0:
            if j >= 0 and word1[i] == word2[j]:
                rightMatched += 1
                j -= 1
            rightMatchedCharLen[i] = rightMatched
            i -= 1
        
        i, j = 0, 0
        res = []
        isChangeAllowed = True
        while i < m and j < n:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif (
                isChangeAllowed and 
                i + 1 < m and 
                rightMatchedCharLen[i + 1] >= n - j - 1):
                    res.append(i)
                    isChangeAllowed = False
                    j += 1
            i += 1
        
        return res if j == n else []