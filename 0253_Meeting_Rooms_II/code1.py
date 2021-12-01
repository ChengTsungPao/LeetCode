class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 一開始依開始時間排序，再依次將結束時間放進heap，若結束時間比開始時間還早的時間踢出heap
        
        ans = 0
        heap = []
        
        for start, end in sorted(intervals):
            
            while heap and heap[0] <= start:
                heapq.heappop(heap)
                
            heapq.heappush(heap, end)
            
            ans = max(ans, len(heap))
            
        return ans