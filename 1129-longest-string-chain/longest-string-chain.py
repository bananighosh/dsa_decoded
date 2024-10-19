class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key = lambda w : -len(w))

        wordIndex = {w:i for i,w in enumerate(words)}
        @cache
        def dfs(i):

            res = 1

            for j, word in enumerate(words[i]):
                nWord = words[i]

                pred = nWord[:j] + nWord[j+1:]

                if pred in wordIndex:
                    res = max(res, 1 + dfs(wordIndex[pred]))
            
            return res
        ans = 0
        for i in range(len(words)):
            ans = max(ans, dfs(i))

        return ans