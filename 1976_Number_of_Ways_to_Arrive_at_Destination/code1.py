class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        
        graph = collections.defaultdict(list)
        for nodei, nodej, cost in roads:
            graph[nodei].append((nodej, cost))
            graph[nodej].append((nodei, cost))
            
        minCost = -1
        visited = set()
        heap = [(0, 0)]
        prevMinCostMemo = {}
        
        while heap:
            currentCost, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            visited.add(node)
            
            prevMinCostMemo[node] = currentCost
            
            if node == n - 1:
                minCost = currentCost
                break

            for nextNode, cost in graph[node]:                    
                heapq.heappush(heap, (currentCost + cost, nextNode))
                
        ans = 0
        memo = {}
        visited = set()
        def dfs(node, currentCost):
            
            if node in visited or currentCost + prevMinCostMemo.get(node, 0) > minCost:
                return 0
            
            if node not in memo:
            
                if node == 0:
                    return currentCost == minCost

                visited.add(node)

                ans = 0
                for nextNode, cost in graph[node]:
                    ans += dfs(nextNode, currentCost + cost)

                visited.remove(node)
                
                memo[node] = ans
                
            return memo[node]
        
        return dfs(n - 1, 0) % MOD