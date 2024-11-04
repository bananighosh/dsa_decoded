class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split(" ")
        n = len(words)

        first_word = words[0]
        last_word = words[- 1]

        if first_word[0] != last_word[ - 1]:
            return False

        for i, word in enumerate(words):
            if i == len(words)-1:
                break
            if words[i][-1] != words[i + 1][0]:
                return False

        return True

        