class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        # Prim's algorithm
        
        graph = collections.defaultdict(list)
        for node, nextNode, cost in connections:
            graph[node].append((nextNode, cost))
            graph[nextNode].append((node, cost))
        
        randomNode = random.randrange(1, n + 1)
        if not graph[randomNode]:
            return -1
        heap = [(0, graph[randomNode][0][0])]  
        
        ans = 0
        visited = set()
        
        while heap and len(visited) < n:
            cost, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            ans += cost
            visited.add(node)
            
            for nextNode, cost in graph[node]:
                if nextNode in visited:
                    continue
                heapq.heappush(heap, (cost, nextNode))

        return ans if len(visited) == n else -1