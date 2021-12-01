class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 概念: 一開始依時間排序，若為開始時間target = 1，結束時間則target = -1，接著依時間統計target之總和
        
        ans = 0
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
            
        times.sort()

        count = 0
        for time, target in times:
            count += target
            ans = max(ans, count)
            
        return ans