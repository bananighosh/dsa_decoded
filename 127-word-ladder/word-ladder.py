class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjDict = defaultdict(set)
        hashSet = set(wordList)
        letters = "abcdefghijklmnopqrstuvwxyz"
        for word in [beginWord, *wordList]:
            for i in range(len(word)):
                for letter in letters:
                    nWord = word[:i] + letter + word[i+1:]
                    if nWord in hashSet:
                        adjDict[word].add(nWord)
                        adjDict[nWord].add(word) 

        vis = set()
        st = [beginWord]
        dist = 0
        while st:
            curr = []
            dist += 1
            for word in st:
                if word == endWord:
                    return dist
                if word in vis:
                    continue
                vis.add(word)
                for words in adjDict[word]:
                    if words in vis:
                        continue
                    curr.append(words)
            st = curr
        return 0


                
