class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        
        graph = collections.defaultdict(list)
        for nodei, nodej, cost in roads:
            graph[nodei].append((nodej, cost))
            graph[nodej].append((nodei, cost))
        
        ans = 0
        heap = [(0, 0)]
        
        minCost = [float("inf")] * n
        minCost[0] = 0
        
        count = [0] * n
        count[0] = 1
        
        while heap:
            currentCost, node = heapq.heappop(heap)

            for nextNode, cost in graph[node]:  
                if minCost[nextNode] > currentCost + cost:
                    minCost[nextNode] = currentCost + cost
                    heapq.heappush(heap, (currentCost + cost, nextNode))
                    count[nextNode] = count[node]
                elif minCost[nextNode] == currentCost + cost:
                    count[nextNode] += count[node]
                
        return count[n - 1] % MOD