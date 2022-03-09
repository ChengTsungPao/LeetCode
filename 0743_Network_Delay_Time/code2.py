class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))
    
        
        costs = {}
        heap = [(0, k)]
        
        while heap:
            curTime, node = heapq.heappop(heap)
            
            if node in costs:
                continue
                
            costs[node] = curTime
            
            for nextNode, time in graph[node]:
                if nextNode not in costs:
                    heapq.heappush(heap, (curTime + time, nextNode))
        
        return max(costs.values()) if len(costs) == n else -1