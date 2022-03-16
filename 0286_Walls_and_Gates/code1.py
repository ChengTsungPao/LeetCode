class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        m = len(rooms)
        n = len(rooms[0])
        
        gate = 0
        obstacle = -1
        
        stack = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == gate:
                    stack.append((i, j))
        
        step = 1
        visited = set()

        while stack:
            
            newStack = []
            
            while stack:
                i, j = stack.pop()
                
                for i_, j_ in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if not (0 <= i_ < m and 0 <= j_ < n) or (i_, j_) in visited or \
                       rooms[i_][j_] == gate or rooms[i_][j_] == obstacle:
                        continue
                        
                    visited.add((i_, j_))
                    newStack.append((i_, j_))
                    rooms[i_][j_] = step
     
            stack = newStack.copy()
            step += 1