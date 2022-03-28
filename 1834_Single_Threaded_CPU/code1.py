class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        n = len(tasks)
        tasks = sorted([(tasks[index][0], tasks[index][1], index) for index in range(n)])
        
        ans = []
        heap = []
        time = 0
        index = 0
        
        while heap or index < n:
            # CPU IDLE
            if heap == [] and index < n:
                enqueueTime, processingTime, taskIndex = tasks[index]
                heapq.heappush(heap, (processingTime, taskIndex, enqueueTime))
                index += 1          
                time = enqueueTime

            # Running Process
            processingTime, taskIndex, enqueueTime = heapq.heappop(heap)
            ans.append(taskIndex)
            time += processingTime

            # Ready Process
            while index < n and tasks[index][0] <= time:
                enqueueTime, processingTime, taskIndex = tasks[index]
                heapq.heappush(heap, (processingTime, taskIndex, enqueueTime))
                index += 1
                
        return ans