class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        
        memo = {}
        def recur(index, bricks, ladders):
            
            if (index, bricks, ladders) not in memo:
            
                if bricks < 0 or ladders < 0:
                    return -float("inf")

                if index + 1 >= n:
                    return 0

                ans = 0
                h = heights[index + 1] - heights[index]
                if h <= 0:
                    ans = max(ans, recur(index + 1, bricks, ladders) + 1)
                else:
                    ans = max(ans, recur(index + 1, bricks - h, ladders) + 1, recur(index + 1, bricks, ladders - 1) + 1)
                    
                memo[index, bricks, ladders] = ans
                
            return memo[index, bricks, ladders]
        
        return recur(0, bricks, ladders)