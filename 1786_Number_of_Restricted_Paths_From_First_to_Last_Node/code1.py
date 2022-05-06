class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for node, nextNode, cost in edges:
            graph[node].append((nextNode, cost))
            graph[nextNode].append((node, cost))
            
            
        heap = [(0, n)]
        cache = {}
        while heap and len(cache) < n:
            score, node = heapq.heappop(heap)
            
            if node in cache:
                continue
            cache[node] = score
            
            for nextNode, cost in graph[node]:
                if nextNode in cache:
                    continue
                
                heapq.heappush(heap, (score + cost, nextNode))
                

        memo = {}
        def recur(node):
            
            if node not in memo:
            
                if node == n:
                    return 1

                ans = 0
                for nextNode, cost in graph[node]:
                    if cache[node] > cache[nextNode]:
                        ans += recur(nextNode)
                        
                memo[node] = ans
                    
            return memo[node]
        
        return recur(1) % (10 ** 9 + 7)