class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        visited.add(source)
        def dfs(node):
            if node == destination:
                return True
            for val in adj[node]:
                if val not in visited:
                    visited.add(val)
                    if dfs(val):
                        return True
            return False   
            
        return dfs(source)
