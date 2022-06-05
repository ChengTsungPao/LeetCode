class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        DRAW = 0
        MOUSEWIN = 1
        CATWIN = 2
        
        n = len(graph)
        
        memo = {}
        def recur(mousePos, catPos, who, visited):
            
            if (mousePos, catPos, who) in memo:
                return memo[mousePos, catPos, who]
         
            if mousePos == catPos:
                return CATWIN
            elif mousePos == 0:
                return MOUSEWIN
            elif (mousePos, catPos, who) in visited:
                return DRAW

            visited.add((mousePos, catPos, who))
            
            if who:     
                ans = CATWIN
                for nextMousePos in graph[mousePos]:                    
                    ret = recur(nextMousePos, catPos, not who, visited)
                    if ret == CATWIN:
                        continue
                        
                    ans = ret
                    if ans == MOUSEWIN:
                        break
            else:        
                ans = MOUSEWIN
                for nextCatPos in graph[catPos]:   
                    if nextCatPos == 0:
                        continue
                        
                    ret = recur(mousePos, nextCatPos, not who, visited)
                    if ret == MOUSEWIN:
                        continue
                    
                    ans = ret
                    if ans == CATWIN:
                        break
            
            if ans != DRAW:
                memo[mousePos, catPos, who] = ans 
                
            return ans
        
        
        for i in range(n):
            count = len(memo)
            ans = recur(1, 2, True, set())
            if ans != DRAW or count == len(memo):
                break
        
        return ans