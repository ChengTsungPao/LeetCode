class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        def recur(room):
            if room in visited:
                return
            
            visited.add(room)
            
            for nextRoom in rooms[room]:
                recur(nextRoom)
                
        recur(0)
        
        return len(visited) == len(rooms)