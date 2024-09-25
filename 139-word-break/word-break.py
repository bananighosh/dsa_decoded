class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = [None]*26
        self.endWord= False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        a = "a"
        root = Trie()
        def addWord( word):
            a = "a"
            roote = root
            for letter in word:
                if roote.children[ord(letter)-ord(a)] is None :
                    roote.children[ord(letter)-ord(a)] = Trie(val = letter)
                roote = roote.children[ord(letter)-ord(a)]
            roote.endWord = True
        for word in wordDict:
            addWord(word)
    
        @cache
        def dfs(i):
            if i == len(s):
                return True
            ans = False
            for word in wordDict:
                n = len(word)
                if s[i:i+n] == word:
                    ans = ans or dfs(i+n)
            return ans
        return dfs(0)
