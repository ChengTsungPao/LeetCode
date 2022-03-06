class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Bellman Ford => "check negative edge" just find the distance array update or not at final loop
        '''
        
        distance = [float("inf")] * n
        distance[src] = 0
        
        for _ in range(min(k + 1, n - 1)):
            preDistance = distance.copy()
            
            for start, end, weight in flights:
                if preDistance[start] != float("inf"):
                    distance[end] = min(distance[end], preDistance[start] + weight)
                    
        return distance[dst] if distance[dst] != float("inf") else -1