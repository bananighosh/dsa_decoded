

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        inDegree = {i:0 for i in range(numCourses)}

        for course, preq in prerequisites:
            adjList[course].append(preq)
            inDegree[preq] += 1
        
        queue = deque()

        for i, val in inDegree.items():
            if val == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nodes in adjList[node]:
                inDegree[nodes] -= 1
                if inDegree[nodes] == 0:
                    queue.append(nodes)
        return count == numCourses

        
        