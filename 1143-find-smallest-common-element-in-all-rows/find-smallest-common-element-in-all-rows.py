class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        smallestCommEle = mat[0][0]
        commSet = [set(row) for row in mat]

        for n in mat[0]:
            found = True
            for row in commSet:
                if n not in row:
                    found = False
                    break
            if found:
                return n
        
        return -1

        # commMap = defaultdict()
        # commSet = mat[0]
        # print(commSet)

        # for i in range(1,len(mat)):
        #     currSet = mat[i]
        #     print(currSet)
        #     for n in currSet:
        #         if n in commSet:
        #             print(n)
        #             smallestCommEle = min(smallestCommEle,  n)
        
        # return smallestCommEle
