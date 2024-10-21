class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        #sol 2
        commMap = defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                commMap[mat[i][j]] += 1
        
        for key, val in commMap.items():
            if val == len(mat):
                return key
        
        return -1


        # sol 1
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

        # 1st thought
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
