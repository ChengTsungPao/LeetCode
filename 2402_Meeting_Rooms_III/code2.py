class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        count = collections.defaultdict(int)
        empty, using = list(range(n)), []
        
        meetings.sort()
        
        for start_t, end_t in meetings:
            while using and start_t >= using[0][0]:
                end_room_t, roomid = heapq.heappop(using)
                heapq.heappush(empty, roomid)
                
            if empty:
                end_room_t = end_t
                roomid = heapq.heappop(empty)
            else:
                end_room_t, roomid = heapq.heappop(using)
                end_room_t += end_t - start_t
                
            heapq.heappush(using, (end_room_t, roomid))
            count[roomid] += 1
 
        return min([(-times, roomid) for roomid, times in count.items()])[1]