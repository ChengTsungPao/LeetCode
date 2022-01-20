class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int: 
        
        def recur(workersIndex, bikesBitmap, memo = {}):
            
            if (workersIndex, bikesBitmap) not in memo:
            
                if workersIndex == len(workers):
                    return 0

                ans = float("inf")

                for bikesIndex in range(len(bikes)):
                    if (bikesBitmap >> bikesIndex) % 2:
                        continue 
                        
                    wx, wy = workers[workersIndex]
                    bx, by = bikes[bikesIndex]
                    distance = abs(wx - bx) + abs(wy - by)

                    ans = min(ans, distance + recur(workersIndex + 1, bikesBitmap + 2 ** bikesIndex))

                memo[workersIndex, bikesBitmap] = ans
                    
            return memo[workersIndex, bikesBitmap]
        
        return recur(0, 0)