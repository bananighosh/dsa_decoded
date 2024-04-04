class Solution:
    def reorganizeString(self, s: str) -> str:
        stringCount = Counter(s)
        for kry, val in stringCount.items():
            if val > math.ceil(len(s)/2):
                return ""
        strArray = [(-1*val, key) for key, val in stringCount.items()]
        heapq.heapify(strArray)
        ans = "*"
        while strArray:
            val, key = heapq.heappop(strArray)
            if ans[-1] != key:
                ans += key
                val += 1
            else:
                val2, key2 = heapq.heappop(strArray)
                ans += key2
                val2 += 1
                if val2 != 0:
                    heapq.heappush(strArray,(val2, key2))
            if val != 0:
                heapq.heappush(strArray,(val, key))
    
        return ans[1:]
            




        