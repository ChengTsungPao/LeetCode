class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        ans = []
        
        Running = []
        IDLE = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(IDLE)
        
        time = 0
        for j, runningTime in enumerate(tasks):
            
            time = max(time, j)
            if not IDLE:
                time = max(time, Running[0][0])
            
            while Running and Running[0][0] <= time:
                _, i = heapq.heappop(Running)
                heapq.heappush(IDLE, (servers[i], i))

            _, i = heapq.heappop(IDLE)
            heapq.heappush(Running, (time + runningTime, i))
            ans.append(i)
            
        return ans