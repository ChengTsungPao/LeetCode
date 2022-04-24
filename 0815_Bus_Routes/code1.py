class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        n = len(routes)
        stationRoutes = collections.defaultdict(set)
        
        for route in range(n):
            for station in routes[route]:
                stationRoutes[station].add(route)
                
        graph = collections.defaultdict(set)
        for station in stationRoutes.keys():
            for route1 in stationRoutes[station]:
                for route2 in stationRoutes[station]:
                    if route1 != route2:
                        graph[route1].add(route2)
                        graph[route2].add(route1)
                        

        visited = set()
        que = collections.deque()
        for node in stationRoutes[source]:
            visited.add(node)
            que.appendleft((node, 1))
        
        while que:
            node, step = que.pop()
            
            if node in stationRoutes[target]:
                return step
            
            for nextNode in graph[node]:
                if nextNode in visited:
                    continue
                    
                visited.add(nextNode)
                que.appendleft((nextNode, step + 1))
                
        return -1