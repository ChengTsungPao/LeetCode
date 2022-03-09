class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = collections.defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((prob, v))
            graph[v].append((prob, u))
        
        ans = 0
        probs = {}
        heap = [(-1, start)]
        
        while heap:
            curProb, node = heapq.heappop(heap)
            curProb *= -1

            if node in probs:
                continue
                
            if node == end:
                return curProb
            
            probs[node] = curProb
            
            for prob, nextNode in graph[node]:
                if nextNode not in probs:
                    heapq.heappush(heap, (-curProb * prob, nextNode))
         
        return ans