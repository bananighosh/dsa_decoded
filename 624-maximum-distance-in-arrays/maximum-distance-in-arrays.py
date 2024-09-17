class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max_dist = 0
        n = len(arrays)
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, n):
            print(arrays[i], min_val, max_val)
            max_dist = max(max_dist, abs(max_val - arrays[i][0]), abs(arrays[i][-1] - min_val))
            
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_dist


        