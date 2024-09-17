class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max_dist = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for arr in arrays[1:]:
            max_dist = max(max_dist, abs(max_val - arr[0]), abs(arr[-1] - min_val))
            
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        
        return max_dist