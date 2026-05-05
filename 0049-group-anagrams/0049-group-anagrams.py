class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            # sorted_word = ''.join(sorted(s))
            # sorted_word = tuple(sorted(s))
            res[tuple(sorted(s))].append(s)
        
        return list(res.values())
        