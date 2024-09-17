class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1_set = s1.split()
        s2_set = s2.split()

        freq1 = Counter(s1_set)
        freq2 = Counter(s2_set)

        res = []

        for key, value in freq1.items():
            if value == 1 and key not in freq2:
                res.append(key) 
        
        print(res)
        for key, value in freq2.items():
            if value == 1 and key not in freq1:
                res.append(key)

        
        # print(res, freq2, freq1)
        # for word in res:
        #     if word in freq2:
        #         res.remove(word)

        return res
