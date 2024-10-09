class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        n1, n2 = len(sentence1), len(sentence2)

        if n1 != n2:
            return False

        curr_word_similar_pairs = defaultdict(set)

        for word1, word2 in similarPairs:
            curr_word_similar_pairs[word1].add(word2)
            curr_word_similar_pairs[word2].add(word1)
            
            
        print(curr_word_similar_pairs)
        for i in range(n1):
            print(curr_word_similar_pairs[sentence1[i]], sentence1[i], sentence2[i])
            if sentence1[i] == sentence2[i] or sentence2[i] in curr_word_similar_pairs[sentence1[i]]:
                continue
            return False
        
        return True
        