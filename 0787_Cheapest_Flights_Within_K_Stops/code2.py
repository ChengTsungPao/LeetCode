class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:  
        
        graph = collections.defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))
   
        heap = [(0, 0, src)]
        found = {src: 0}
        ans = float("inf")
        
        while heap:
            step, score, node = heapq.heappop(heap)
            
            if node == dst:
                ans = min(ans, score)
            
            for nextNode, cost in graph[node]:
                newScore = score + cost
                
                if newScore > found.get(nextNode, float("inf")) or step > k:
                    continue
  
                found[nextNode] = newScore
                heapq.heappush(heap, (step + 1, newScore, nextNode))

        return ans if ans != float("inf") else -1