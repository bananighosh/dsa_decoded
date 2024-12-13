class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        pq = []

        for i, val in enumerate(nums):
            heappush(pq, (val,i))
        
        score = 0
        visited = [False] * n

        while pq:
            val, i = heappop(pq)

            if visited[i]:
                continue
            
            score += val
            visited[i] = True

            if i - 1 >= 0:
                visited[i - 1] = True
            if i + 1 < n:
                visited[i + 1] = True
        
        return score
        