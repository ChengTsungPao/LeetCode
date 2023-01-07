class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        count = collections.defaultdict(int)
        
        # empty room (heap)
        empty = list(range(n))
        
        # when need room
        meetings = {start_t: end_t for start_t, end_t in meetings}
        
        # using the room: {end_t: [roomid1, roomid2...]} (heap)
        using = collections.defaultdict(list) 
        
        # wating for room: [using time, ...] (que)
        waiting = collections.deque() 
        
        heapq.heapify(empty)
        
        maxStartTime = max(meetings.keys())
        minTime, maxTime = min(meetings.keys()), max(meetings.values())
        
        time = 0
        for time in range(minTime, maxTime + 1):
            
            # waiting people use first, when using room time's up
            while waiting and time in using:
                roomid = heapq.heappop(using[time])
                if not using[time]: del using[time]
                room_end_t = time + waiting.popleft()
                heapq.heappush(using[room_end_t], roomid)
                count[roomid] += 1
            
            # release time's up room
            if time in using:
                for roomid in using[time]:
                    heapq.heappush(empty, roomid)
                del using[time]
            
            # current time someone need room
            if time in meetings:
                start_t, end_t = time, meetings[time]

                if empty:
                    roomid = heapq.heappop(empty)
                    heapq.heappush(using[end_t], roomid)
                    count[roomid] += 1
                else:
                    waiting.append(end_t - start_t)
                    
            if empty and not waiting and time > maxStartTime:
                break
        
        # Someone still waiting
        if waiting:
            endTimeRoomHeap = [(time, roomid) for roomid in empty]
            
            for room_end_t, roomids in using.items():
                for roomid in roomids:
                    endTimeRoomHeap.append((room_end_t, roomid))
            heapq.heapify(endTimeRoomHeap)

            while waiting:
                curTime, roomid = heapq.heappop(endTimeRoomHeap)
                room_end_t = curTime + waiting.popleft()
                heapq.heappush(endTimeRoomHeap, (room_end_t , roomid))
                count[roomid] += 1
                
        return min([(-times, roomid) for roomid, times in count.items()])[1]