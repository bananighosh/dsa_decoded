class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hashMap = [set(row) for row in mat ]
        for num in mat[0]:
            flag = True
            for row in hashMap:
                if num not in row:
                    flag = False
                    break
            if flag:
                return num
        return -1
        