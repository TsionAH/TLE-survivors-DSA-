from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visted = set()
        visted.add(source)
        queue = deque([source])
        while queue:
            val = queue.popleft()
            if val == destination:
                return True
            for i in adj[val]:
                if i not in visted:
                    visted.add(i)
                    queue.append(i)
        return False

        