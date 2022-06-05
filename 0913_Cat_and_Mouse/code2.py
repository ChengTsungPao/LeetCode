class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        DRAW = 0
        MOUSEWIN = 1
        CATWIN = 2
        
        MOUSETURN = True
        CATTURN = False
        
        n = len(graph)
        degree = collections.defaultdict(int)
        for mousePos in range(n):
            for catPos in range(n):
                degree[mousePos, catPos, MOUSETURN] = len(graph[mousePos])
                degree[mousePos, catPos, CATTURN] = len(graph[catPos]) - (0 in graph[catPos])
        
        que = collections.deque()
        result = collections.defaultdict(int)
        for pos in range(1, n):
            for turn in [MOUSETURN, CATTURN]:
                result[0, pos, turn] = MOUSEWIN
                result[pos, pos, turn] = CATWIN
                que.appendleft((0, pos, turn))
                que.appendleft((pos, pos, turn))
                
        while que:
            mousePos, catPos, turn = que.pop()
            winner = result[mousePos, catPos, turn]
            
            if turn == MOUSETURN:
                for preCatPos in graph[catPos]:
                    if result[mousePos, preCatPos, CATTURN] != DRAW or preCatPos == 0:
                        continue
                        
                    if winner == CATWIN:
                        result[mousePos, preCatPos, CATTURN] = CATWIN
                        que.appendleft((mousePos, preCatPos, CATTURN))
                    else:
                        degree[mousePos, preCatPos, CATTURN] -= 1
                        if degree[mousePos, preCatPos, CATTURN] == 0:
                            result[mousePos, preCatPos, CATTURN] = MOUSEWIN
                            que.appendleft((mousePos, preCatPos, CATTURN))
                            
            else:
                for preMousePos in graph[mousePos]:
                    if result[preMousePos, catPos, MOUSETURN] != DRAW:
                        continue
                    
                    if winner == MOUSEWIN:
                        result[preMousePos, catPos, MOUSETURN] = MOUSEWIN
                        que.appendleft((preMousePos, catPos, MOUSETURN))
                    else:
                        degree[preMousePos, catPos, MOUSETURN] -= 1
                        if degree[preMousePos, catPos, MOUSETURN] == 0:
                            result[preMousePos, catPos, MOUSETURN] = CATWIN
                            que.appendleft((preMousePos, catPos, MOUSETURN))                     
                        
                
        return result[1, 2, MOUSETURN]