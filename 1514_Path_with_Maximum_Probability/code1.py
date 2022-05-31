class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = collections.defaultdict(list)
        for (node, nextNode), prob in zip(edges, succProb):
            graph[node].append((nextNode, prob))
            graph[nextNode].append((node, prob))
            
        
        heap = [(-1, start)]
        visited = set()
        
        while heap:
            prob, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            if node == end:
                return -prob
            
            visited.add(node)
            
            for nextNode, nextProb in graph[node]:
                if nextNode in visited:
                    continue
                    
                heapq.heappush(heap, (-abs(prob * nextProb), nextNode))
                
        return 0