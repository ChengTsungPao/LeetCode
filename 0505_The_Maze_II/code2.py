class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        想法: 既然都需要走完BFS，那在que內的次序就不影響結果了阿! => 用stack
        修正: 在程式第50行有剪枝，因此若以步數(每次action算一步)作為排序，會過濾掉更多種可能，所以使用que的排序策略會比stack好
        '''

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
        found = {(start[0], start[1]): 0}
        stack = [(0, start[0], start[1])]
        
        while stack:
            score, x, y = stack.pop()

            if destination == [x, y]:
                ans = min(ans, score)

            for action in actions:
                nextX, nextY = find_next_pos(x, y, action)

                if (nextX == x and nextY == y):
                    continue
                
                distance = abs(nextX - x) + abs(nextY - y)
                if score + distance > found.get((nextX, nextY), float("inf")):
                    continue
                    
                found[nextX, nextY] = score + distance
                stack.append((score + distance, nextX, nextY))
                    
        return ans if ans != float("inf") else -1