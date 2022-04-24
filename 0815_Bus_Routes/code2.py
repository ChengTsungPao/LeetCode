class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        n = len(routes)
        stationRoutes = collections.defaultdict(set)
        
        for route in range(n):
            for station in routes[route]:
                stationRoutes[station].add(route)
                        

        visited = set([source])
        que = collections.deque([(source, 0)])
        
        while que:
            station, step = que.pop()
            
            if station == target:
                return step
            
            for route in stationRoutes[station]:
                for nextStation in routes[route]:
                    if nextStation in visited:
                        continue

                    visited.add(nextStation)
                    que.appendleft((nextStation, step + 1))
                    
                routes[route] = []
                
        return -1  