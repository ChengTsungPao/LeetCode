class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        def find_next_pos(x, y, action): 
            
            if action == "up":
                while x - 1 >= 0 and maze[x - 1][y] == 0:
                    x -= 1
            elif action == "down":
                while y - 1 >= 0 and maze[x][y - 1] == 0:
                    y -= 1
            elif action == "left":
                while x + 1 < height and maze[x + 1][y] == 0:
                    x += 1
            elif action == "right":
                while y + 1 < width and maze[x][y + 1] == 0:
                    y += 1
            else:
                pass
            
            return x, y
        
        
        height = len(maze)
        width = len(maze[0])
                
        que = collections.deque()
        found = set()
        
        que.appendleft(tuple(start))
        found.add(tuple(start))
        
        actions = ["up", "down", "left", "right"]
        
        while que:
            x, y = que.pop()
            
            for action in actions:
                x_, y_ = find_next_pos(x, y, action)
                
                if [x_, y_] == destination:
                    return True
                
                if (x_, y_) not in found:
                    que.appendleft((x_, y_))
                    found.add((x_, y_))
                    
        return False
