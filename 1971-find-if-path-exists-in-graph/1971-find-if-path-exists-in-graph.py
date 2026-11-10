class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        visited.add(source)
        stack = [source]
        while stack:
            val = stack.pop()
            if val == destination:
                return True
            for i in adj[val]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)

        return False
