class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for string in strings:
            key = []
            for i in range(len(string)-1):
                key.append((ord(string[i+1]) - ord(string[i]))%26)
            hashMap["".join(str(key))].append(string)
        return hashMap.values()
        