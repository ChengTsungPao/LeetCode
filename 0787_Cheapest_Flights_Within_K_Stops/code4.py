class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        for node, nextNode, cost in flights:
            graph[node].append((nextNode, cost))
            
        
        que = collections.deque([(0, 0, src)])
        scores = {src: 0}
        ans = float("inf")
        
        while que:
            step, score, node = que.pop()
            
            if node == dst:
                ans = min(ans, score)
                
            if step == k + 1:
                continue
                
            for nextNode, cost in graph[node]:
                newScore = score + cost
                if newScore > scores.get(nextNode, float("inf")):
                    continue
                    
                que.appendleft((step + 1, newScore, nextNode))
                scores[nextNode] = newScore
                
        return ans if ans != float("inf") else -1