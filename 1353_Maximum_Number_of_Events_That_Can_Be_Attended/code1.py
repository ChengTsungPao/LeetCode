class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        # 當前時間點，最快結束的活動先參加
        
        status = collections.defaultdict(list)
        for start, end in events:
            status[start].append(end)
        
        count = 0
        heap = []
        for time in range(10**5 + 1):
            for endTime in status[time]:
                heapq.heappush(heap, endTime)
                
            while heap:
                endTime = heapq.heappop(heap)
                if endTime >= time:
                    count += 1
                    break

        return count