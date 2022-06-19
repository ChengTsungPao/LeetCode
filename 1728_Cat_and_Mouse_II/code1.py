class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        
        def allParents(mousePos, catPos, turn):
            position = []
            if turn == MOUSETURN:
                i, j = catPos
                for c1, c2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    for k in range(catJump + 1):
                        x, y = i + c1 * k, j + c2 * k
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "#":
                            break
                        position.append((mousePos, (x, y), CATTURN))
            else:
                i, j = mousePos
                for c1, c2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    for k in range(mouseJump + 1):
                        x, y = i + c1 * k, j + c2 * k
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "#":
                            break
                        position.append(((x, y), catPos, MOUSETURN))
            return position        

        def allChildrenWin(mousePos, catPos, turn):
            if turn == MOUSETURN:
                i, j = mousePos
                for c1, c2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    for k in range(mouseJump + 1):
                        x, y = i + c1 * k, j + c2 * k
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "#":
                            break
                        if result[(x, y), catPos, CATTURN] != CATWIN:
                            return False
            else:
                i, j = catPos
                for c1, c2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    for k in range(catJump + 1):
                        x, y = i + c1 * k, j + c2 * k
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "#":
                            break
                        if result[mousePos, (x, y), MOUSETURN] != MOUSEWIN:
                            return False
            return True
        
        m = len(grid)
        n = len(grid[0])
        
        MOUSEWIN = 1
        CATWIN = 2
        
        MOUSETURN = True
        CATTURN = False
        
        # Get the mouse cat food position
        startMousePos = (-1, -1)
        startCatPos = (-1, -1)
        foodPos = (-1, -1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "M":
                    startMousePos = (i, j)
                elif grid[i][j] == "C":
                    startCatPos = (i, j)
                elif grid[i][j] == "F":
                    foodPos = (i, j)
        
        # Initial state
        result = collections.defaultdict(int)
        que = collections.deque()   
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "#" and grid[i][j] != "F":
                    # mouse get food
                    mousePos = foodPos[0], foodPos[1]
                    catPos = (i, j)
                    que.appendleft((mousePos, catPos, MOUSETURN))
                    que.appendleft((mousePos, catPos, CATTURN))
                    result[mousePos, catPos, MOUSETURN] = MOUSEWIN
                    result[mousePos, catPos, CATTURN] = MOUSEWIN
                    
                    # cat get food
                    mousePos = (i, j)
                    catPos = foodPos[0], foodPos[1]
                    que.appendleft((mousePos, catPos, MOUSETURN))
                    que.appendleft((mousePos, catPos, CATTURN))
                    result[mousePos, catPos, MOUSETURN] = CATWIN
                    result[mousePos, catPos, CATTURN] = CATWIN
                    
                    # mouse and cat in same position
                    mousePos = (i, j)
                    catPos = (i, j)
                    que.appendleft((mousePos, catPos, MOUSETURN))
                    que.appendleft((mousePos, catPos, CATTURN))
                    result[mousePos, catPos, MOUSETURN] = CATWIN
                    result[mousePos, catPos, CATTURN] = CATWIN
        
        # BFS
        playTimes = 0
        while que:
            
            newQue = collections.deque()
            while que:
                mousePos, catPos, turn = que.pop()
                win = result[mousePos, catPos, turn]
            
                for preMousePos, preCatPos, preTurn in allParents(mousePos, catPos, turn):
                    if result[preMousePos, preCatPos, preTurn] != 0:
                        continue
                    
                    # mouse win
                    if preTurn == MOUSETURN and win == MOUSEWIN:
                        result[preMousePos, preCatPos, preTurn] = MOUSEWIN
                        newQue.appendleft((preMousePos, preCatPos, preTurn))
                    elif preTurn == CATTURN and allChildrenWin(preMousePos, preCatPos, preTurn):
                        result[preMousePos, preCatPos, preTurn] = MOUSEWIN
                        newQue.appendleft((preMousePos, preCatPos, preTurn))
                    
                    # cat win
                    if preTurn == CATTURN and win == CATWIN:
                        result[preMousePos, preCatPos, preTurn] = CATWIN
                        newQue.appendleft((preMousePos, preCatPos, preTurn))
                    elif preTurn == MOUSETURN and allChildrenWin(preMousePos, preCatPos, preTurn):
                        result[preMousePos, preCatPos, preTurn] = CATWIN
                        newQue.appendleft((preMousePos, preCatPos, preTurn))

            que = newQue
            playTimes += 1
            if playTimes >= 1000:
                break
                
        return result[startMousePos, startCatPos, MOUSETURN] == MOUSEWIN