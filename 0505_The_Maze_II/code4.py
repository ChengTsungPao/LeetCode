class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

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
        actions = ["up", "down", "left", "right"]
        
        ans = float("inf")
        found = set()
        heap = [(0, start[0], start[1])]
        
        while heap:
            score, x, y = heapq.heappop(heap)

            if destination == [x, y]:
                return score

            if (x, y) in found:
                continue
            
            found.add((x, y))
            
            for action in actions:
                nextX, nextY = find_next_pos(x, y, action)

                if (nextX == x and nextY == y):
                    continue
                    
                distance = abs(nextX - x) + abs(nextY - y) 
                heapq.heappush(heap, (score + distance, nextX, nextY))
                    
        return -1