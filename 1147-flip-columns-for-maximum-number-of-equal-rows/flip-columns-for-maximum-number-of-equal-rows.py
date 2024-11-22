class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # if the 1st ele is 0, we keep the row as is
        # if the 1st ele is 1, we will take the complement of the row and add to the freq map

        freq_map = Counter()

        for row in matrix:
            curr_ele = tuple(ele if row[0] == 0 else 1 - ele for ele in row)
            
            freq_map[curr_ele] += 1

        return max(freq_map.values()) 
        