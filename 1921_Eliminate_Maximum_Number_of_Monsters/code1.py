class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        catchTimes = [d / s for d, s in zip(dist, speed)]
        heapq.heapify(catchTimes)
        
        ans = time = 0
        while catchTimes:
            catchTime = heapq.heappop(catchTimes)
            if catchTime - time > 0:
                ans += 1
                time += 1
            else:
                break
                
        return ans