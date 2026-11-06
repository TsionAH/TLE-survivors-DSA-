class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        key = set()
        
        def dfs(node):
            if node in key:
                return
            
            key.add(node)
            for val in rooms[node]:
                dfs(val)
                
           
        dfs(0)
        return len(key) == len(rooms)