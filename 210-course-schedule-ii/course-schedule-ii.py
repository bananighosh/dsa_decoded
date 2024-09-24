class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        in_degree = [0] * numCourses
        for i, j in prerequisites:
            adjList[i].append(j)
            in_degree[j] += 1
        count = 0
        queue = deque()
        for i, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(i)
        order = []
        while queue:
            node = queue.popleft()
            count += 1
            order.append(node)
            for nodes in adjList[node]:
                in_degree[nodes] -= 1
                if in_degree[nodes] == 0:
                    queue.append(nodes)
        if count == numCourses:
            return order[::-1]
        return []
        