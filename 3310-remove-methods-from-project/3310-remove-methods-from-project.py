class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in invocations:
            adj[u].append(v)
        
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if visited[v]:
                    continue
                dfs(v)
        dfs(k)

        can_remove = False
        for u, v in invocations:
            if not visited[u] and visited[v]:
                can_remove = True
                break
        
        if can_remove:
            return list(range(n))
        
        return [i for i in range(n) if not visited[i]]
        