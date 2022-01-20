class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        actionTable = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        
        def getScore(i, j, action):
            di, dj = actionTable[action]
            return abs(heights[i + di][j + dj] - heights[i][j])
            
            
        heap = [(0, 0, 0)]
        found = {(0, 0): 0}

        while heap:
            score, i, j = heapq.heappop(heap)

            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                return score
            
            for action in actionTable.keys():
                di, dj = actionTable[action]
                i_, j_ = i + di, j + dj
                
                if not (0 <= i_ < len(heights) and 0 <= j_ < len(heights[0])):
                    continue
                
                newScore = max(score, getScore(i, j, action))
                if newScore >= found.get((i_, j_), float("inf")):
                    continue
                
                found[i_, j_] = newScore
                heapq.heappush(heap, (newScore, i_, j_))
             
        return float("inf")