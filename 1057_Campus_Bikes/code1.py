class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:  
        
        distance = []
        
        for w in range(len(workers)):
            wx, wy = workers[w]
            
            for b in range(len(bikes)):
                bx, by = bikes[b]   
                
                d = abs(wx - bx) + abs(wy - by)
                distance.append((d, w, b))
                
        distance.sort()
        
        
        ans = [0] * len(workers)
        workerFound = set()        
        bikeFound = set()

        for d, w, b in distance:
            if w in workerFound or b in bikeFound:
                continue
                
            workerFound.add(w)
            bikeFound.add(b)
            
            ans[w] = b
            
        return ans