# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        direction = {
            'U': (-1,  0),
            'D': ( 1,  0),
            'L': ( 0, -1),
            'R': ( 0,  1)
        }
        
        rDirection = {
            'U': 'D',
            'D': 'U',
            'L': 'R',
            'R': 'L'
        }
        
        targetPosition = (float("inf"), float("inf"))
        
        graph = {}
        def createMap(i, j):
            nonlocal targetPosition
            
            if master.isTarget():
                targetPosition = (i, j)
                graph[i, j] = 2

            for d in direction.keys():
                di, dj = direction[d]
                i_, j_ = i + di, j + dj
                if (i_, j_) in graph:
                    continue

                if master.canMove(d):
                    graph[i_, j_] = 1
                    
                    master.move(d)
                    createMap(i_, j_)
                    master.move(rDirection[d])
                else:
                    graph[i_, j_] = 0

        createMap(0, 0)
        
        if targetPosition[0] == float("inf"): 
            return -1
        
        visited = set([(0, 0)])
        que = collections.deque([(0, 0, 0)])
        
        while que:
            i, j, step = que.pop()
            
            if targetPosition == (i, j):
                return step
            
            for di, dj in direction.values():
                i_, j_ = i + di, j + dj
                if (i_, j_) in visited or (i_, j_) not in graph or graph[i_, j_] == 0:
                    continue
                
                visited.add((i_, j_))
                que.appendleft((i_, j_, step + 1))
                
        return -1