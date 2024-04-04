class Solution:
    def reorganizeString(self, s: str) -> str:
        stringCount = Counter(s)
        for kry, val in stringCount.items():
            if val > math.ceil(len(s)/2):
                return ""
        strArray = sorted([(val, key) for key, val in stringCount.items()], key = lambda x : x[0])
        ans = "*"
        while strArray:
            print(strArray)
            val, key = strArray.pop()
            if ans[-1] != key:
                ans += key
                val -= 1
            else:
                val2, key2 = strArray.pop()
                ans += key2
                val2 -= 1
                if val2 != 0:
                    strArray.append((val2, key2))
            if val != 0:
                strArray.append((val, key))
            strArray = sorted(strArray, key = lambda x : x[0])
        return ans[1:] 
            




        