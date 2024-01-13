class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        # n = len(s)
        # i = j = 0
        # if n % 2 == 0:
        #     j = n // 2 - 1
        # else:
        #     j = (n - 1) // 2  - 1 

        # v_count = 0
        # # vowel_arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # vowel_arr = set('aeiouAEIOU')
        # def vowel_count(v_count, s, i, j, vowel_arr):

        #     while i < j and j < n:
        #         if s[i] in vowel_arr:
        #             v_count += 1
        #             i += 1
        #         elif s[j] in vowel_arr:
        #             v_count -= 1
        #             j += 1
            
        #     return vowel_count
        
        # return vowel_count(v_count, s, i, j, vowel_arr) == 0

        n = len(s)
        mid = n // 2

        first_half = s[:mid]
        second_half = s[mid:]

        def vowel_count(str):
            vowel_set = ('aeiouAEIOU')
            v_count = 0
            for c in str:
                if c in vowel_set:
                    v_count += 1

            return v_count
        
        return vowel_count(first_half) == vowel_count(second_half)

                
                
                
                       