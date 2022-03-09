class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 建立有向圖
        graph = collections.defaultdict(list)
        for start, end, time in times:
            graph[start].append((time, end))
        
        # sort才能剪枝
        for start in graph.keys():
            graph[start].sort()
        
        minCosts = {}
        visited = set([k])
        
        def recur(node, curTime):
            
            if curTime > minCosts.get(node, float("inf")):
                return
            
            minCosts[node] = curTime
            
            ans = 0
            for time, nextNode in graph[node]:
                if nextNode in visited:
                    continue
                    
                visited.add(nextNode)
                recur(nextNode, curTime + time)
                visited.remove(nextNode)

        recur(k, 0)
        return max(minCosts.values()) if len(minCosts) == n else -1