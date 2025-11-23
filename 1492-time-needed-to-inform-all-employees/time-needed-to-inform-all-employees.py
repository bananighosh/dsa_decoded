class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """

        def calculateTime(n):
            if manager[n] != -1:
                informTime[n] += calculateTime(manager[n])
                manager[n] = -1
            
            return informTime[n]
        
        for i in range(len(manager)):
            calculateTime(i)
        
        return max(informTime)
        