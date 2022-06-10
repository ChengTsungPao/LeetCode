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
        
        def nextPos(i, j, d):
            direction = {
                'U': (i - 1, j),
                'D': (i + 1, j),
                'L': (i, j - 1),
                'R': (i, j + 1)
            }
            return direction[d]
        
        def prePos(d):
            reDirection = {
                'U': 'D',
                'D': 'U',
                'L': 'R',
                'R': 'L'
            }
            return reDirection[d]
        
        visited = set([(0, 0)])
        def recur(i, j):
            
            if master.isTarget():
                return 0
            
            ret = float("inf")
            for d in ['U','D','L','R']:
                if not master.canMove(d):
                    continue

                i_, j_ = nextPos(i, j, d)
                if (i_, j_) not in visited:
                    master.move(d)
                    visited.add((i_, j_))
                    ret = min(ret, recur(i_, j_) + 1)
                    visited.remove((i_, j_))
                    master.move(prePos(d))
                    
            return ret
        
        ans = recur(0, 0)
        return ans if ans != float("inf") else -1