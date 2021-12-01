class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 概念: 一開始依時間排序，若為開始時間加入record，結束時間則踢出record
        # 注意: intervals仍需要sort，因為若時間相同，結束必須先踢出record
        
        ans = 0
        times = []
        for index, (start, end) in enumerate(sorted(intervals)):
            times.append((start, index))
            times.append((end, index))
            
        times.sort()

        record = set()
        for time, index in times:
            if index in record:
                record.remove(index)
            else:
                record.add(index)
            ans = max(ans, len(record))
            
        return ans