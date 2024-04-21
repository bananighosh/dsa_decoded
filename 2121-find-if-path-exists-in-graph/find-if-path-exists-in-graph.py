class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjdict = defaultdict(set)
        for start, end in edges:
            adjdict[start].add(end)
            adjdict[end].add(start)
        self.vis = set()
        def dfs(node):
            if node in self.vis:
                return False
            if node == destination:
                return True
            self.vis.add(node)
            curr = False
            for nodes in adjdict[node]:
                curr = curr or dfs(nodes)
            return curr
        return dfs(source)

        