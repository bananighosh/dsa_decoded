class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        stringMap = defaultdict(list)
        for s in strings:
            key = []
            for i in range(len(s)-1):
                distance = (ord(s[i+1]) - ord(s[i])) % 26
                key.append(distance)
            stringMap["".join(str(key))].append(s)
        return stringMap.values()
        