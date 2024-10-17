class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjDict = defaultdict(set)
        letters = "abcdefghijklmnopqrstuvwxyz"
        hashSet = set(wordList)
        for word in [beginWord, *wordList]:
            for i in range(len(word)):
                for letter in letters:
                    nword = word[:i] + letter + word[i+1:]
                    if nword in hashSet:
                        adjDict[word].add(nword)
        
        vis = set()
        st = [beginWord]
        dist = 0
        while st:
            dist += 1
            temp = []
            for word in st:
                if word in vis:
                    continue
                vis.add(word)
                if word == endWord:
                    return dist
                for nextWord in adjDict[word]:
                    temp.append(nextWord)
            st = temp
        return 0
            

                
