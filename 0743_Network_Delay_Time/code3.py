class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))
            
        
        costs = {k: 0}
        heap = [(0, k)]
        
        while heap:
            curTime, node = heapq.heappop(heap)
            
            for nextNode, time in graph[node]:
		# 因為放進heap前就記錄答案，造成可能出現比當前答案小的情形，所以需要costs[nextNode] < curTime + time
                if nextNode in costs and costs[nextNode] < curTime + time:
                    continue
                
                # 這樣會造成heap裡面有很多重複的
                costs[nextNode] = curTime + time
                heapq.heappush(heap, (curTime + time, nextNode))
        
        return max(costs.values()) if len(costs) == n else -1