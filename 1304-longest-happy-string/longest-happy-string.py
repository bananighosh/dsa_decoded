class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [(-1*a,"a"), (-1*b, "b"), (-1*c,"c")]
        arr = [(i,j) for i, j in arr if i != 0]
        heapq.heapify(arr)
        ans = "d"
        while arr:
            count1, val1 = heapq.heappop(arr)
            count1 *= -1
            if ans[-1] != val1:
                up = min(2, count1)
                ans += val1*up
                count1 -= up
                if count1 > 0:
                    heapq.heappush(arr, (-1*count1, val1))
            else:
                if not arr:
                    break
                count2, val2 = heapq.heappop(arr)
                count2 *= -1
                ans += val2
                count2 -= 1
                if count2>0:
                    heapq.heappush(arr, (-1*count2, val2))
                heapq.heappush(arr, (-1*count1, val1))
        return ans[1:]