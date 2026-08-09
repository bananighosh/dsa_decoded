class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        rightMatched = 0
        rightMatchedCharLen = [0] * n
        i, j = n - 1, m - 1

        while i >= 0:
            if j >= 0 and word1[i] == word2[j]:
                rightMatched += 1
                j -= 1
            rightMatchedCharLen[i] = rightMatched
            i -= 1
        
        i, j = 0, 0
        res = []
        isChangeAllowed = True
        while i < n and j < m:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif (
                isChangeAllowed and 
                i + 1 < n and 
                rightMatchedCharLen[i + 1] >= m - j - 1):
                    res.append(i)
                    isChangeAllowed = False
                    j += 1
            i += 1
        
        return res if j == m else []