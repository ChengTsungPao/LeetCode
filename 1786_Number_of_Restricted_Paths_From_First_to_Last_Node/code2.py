class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        
        graph = collections.defaultdict(list)
        for node, nextNode, cost in edges:
            graph[node].append((nextNode, cost))
            graph[nextNode].append((node, cost))
            
        heap = [(0, n)]
        cache = [-1] * (n + 1)
        dp = [0] * (n + 1)
        dp[n] = 1
        
        while heap:
            score, node = heapq.heappop(heap)
            
            if cache[node] >= 0:
                continue
            cache[node] = score
            
            for nextNode, cost in graph[node]:
                
                if cache[nextNode] >= 0 and cache[node] > cache[nextNode]:
                    dp[node] += dp[nextNode]
                    dp[node] %= MOD 
                    
                if cache[nextNode] >= 0:
                    continue
                
                heapq.heappush(heap, (score + cost, nextNode))
            
            # 接下來所有的權重都會比node=1大，所以break
            if node == 1:
                break
        
        return dp[1]