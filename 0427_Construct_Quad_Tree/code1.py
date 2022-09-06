"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)
        preSum = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                preSum[i][j] += grid[i - 1][j - 1] + preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1]
                
        def getGridSum(x1, y1, x2, y2):
            return preSum[x2 + 1][y2 + 1] - preSum[x1][y2 + 1] - preSum[x2 + 1][y1] + preSum[x1][y1]
                
        def recur(x1, y1, x2, y2):
            if getGridSum(x1, y1, x2, y2) == 0 or getGridSum(x1, y1, x2, y2) == (x2 - x1 + 1) * (y2 - y1 + 1):
                return Node(grid[x1][y1], 1, None, None, None, None)
            
            x3, y3 = (x1 + x2) // 2, (y1 + y2) // 2
            
            topLeft     = recur(x1 + 0, y1 + 0, x3 + 0, y3 + 0)
            topRight    = recur(x1 + 0, y3 + 1, x3 + 0, y2 + 0)
            bottomLeft  = recur(x3 + 1, y1 + 0, x2 + 0, y3 + 0)
            bottomRight = recur(x3 + 1, y3 + 1, x2 + 0, y2 + 0)
            
            val = topLeft.val or topRight.val or bottomLeft.val or bottomRight.val
            
            return Node(val, 0, topLeft, topRight, bottomLeft, bottomRight)
        
        return recur(0, 0, n - 1, n - 1)