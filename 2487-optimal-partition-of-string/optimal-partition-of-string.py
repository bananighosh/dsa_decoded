class Solution:
    def partitionString(self, s: str) -> int:
        hashSet = set()
        count = 0
        for i in s:
            if i in hashSet:
                count += 1
                hashSet = set()
            hashSet.add(i)
        if hashSet:
            return count + 1
        else:
            return count
        