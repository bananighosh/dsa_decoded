class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        ## Solution 1:
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anagram[sorted_word].append(word)
        
        # return list(anagram.values())

        ## Solution 2:
        # instead of sorting
        for word in strs:
            count = [0] * 26  #initialize the array for a-z 26 chars to 0 count

            for c in word:
                count[ord(c) - ord("a")] += 1

            anagram[tuple(count)].append(word)
        
        return anagram.values()



        