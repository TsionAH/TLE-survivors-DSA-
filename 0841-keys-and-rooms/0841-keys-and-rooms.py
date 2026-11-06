class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        key = set()
        visted_room = {}
        def dfs(node):
            if node == 0:
                for i in rooms[node]:
                    key.add(i)
                
            if node in visted_room:
                return True
            if node!= 0 and  node not in key:
                return False
            visted_room[node] = rooms[node]
            for val in visted_room[node]:
                key.add(val)
                if not dfs(val):
                    return False
            return True
        dfs(0)
        return len(visted_room) == len(rooms)