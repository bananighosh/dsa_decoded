class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        n = len(words)
        
        is_vowel_string = [
            1 if word[0] in vowels and word[-1] in vowels else 0
            for word in words
        ]

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_string[i]

        ans = []
        for l, r in queries:
            ans.append(prefix_sum[r + 1] - prefix_sum[l])
        
        return ans
