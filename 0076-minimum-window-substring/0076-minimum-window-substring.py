class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0 
        start_i = 0
        j = 0
        n = len(s)

        currCount = len(t)
        freq = Counter(t)
        minWindowSize = float("inf")

        while(j < n):
            # print(freq, i, j)
            # if s[j] not in freq:
            #     freq[s[j]] = -1

            if freq[s[j]] > 0:
                currCount -= 1
            freq[s[j]] -= 1

            while currCount == 0:
                if j - i + 1 < minWindowSize:
                    start_i = i
                    minWindowSize = j - i + 1

                freq[s[i]] += 1
                if freq[s[i]] > 0:
                    currCount += 1
                i += 1
            j += 1
        
        return "" if minWindowSize == float("inf") else s[start_i:start_i + minWindowSize]
