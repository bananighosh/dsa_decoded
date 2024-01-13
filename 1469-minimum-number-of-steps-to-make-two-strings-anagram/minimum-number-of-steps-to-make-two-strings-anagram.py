class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # take 2 hashmaps to count the frequencies
        # compare the hashmap result for anagram

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c in s:
            freq1[c] += 1
        
        for c in t:
            freq2[c] += 1
        
        # return freq1 == freq2
        def isAnagram(freq1, freq2):
            if set(freq1.keys()) != set(freq2.keys()):
                return False
            
            for key in freq1:
                if freq1[key] != freq2[key]:
                    return False

            return True

        if isAnagram(freq1, freq2):
            return 0

        def minStepsToAnagram(freq1, freq2):
            min_ops = 0
            for c, freq in freq1.items():
                min_ops += max(0, freq - freq2[c])
            
            return min_ops

        return minStepsToAnagram(freq1, freq2)

