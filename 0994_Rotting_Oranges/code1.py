class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        que, good = collections.deque(), 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good += 1
                elif grid[i][j] == 2:
                    que.appendleft((i, j))
                    
        if good == 0:
            return 0
        
        
        ans = 0
        
        while que:
            nextQue = collections.deque()
            
            while que:
                i, j = que.pop()
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != 1:
                        continue
                    
                    good -= 1
                    grid[x][y] = 2
                    nextQue.appendleft((x, y))
                    
            que = copy.deepcopy(nextQue)
            ans += 1
                
        return ans - 1 if good == 0 else -1
        