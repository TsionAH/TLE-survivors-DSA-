class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # lest convert it in to adjecency list to make things more easier 
        converted = {}
        for node1 , node2 in edges:
            if node1 not in converted:
                converted[node1] = []
            if node2 not in converted:
                converted[node2] = []
            converted[node1].append(node2)
            converted[node2].append(node1)
        visted = set()
        def dfs(node,destination):
            if node in visted:
                return 
            visted.add(node)
            
            if node == destination:
                return True
            for val in converted.get(node,[]):
                if dfs(val,destination):
                    return True
            return False
        return dfs(source,destination)
        
        