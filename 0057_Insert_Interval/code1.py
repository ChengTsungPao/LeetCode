class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        record = [(newInterval[0], 1), (newInterval[1], -1)]
        
        for start, end in intervals:
            record.append((start, 1))
            record.append((end, -1))
              
        
        ans = []
        current = 0

        for time, target in sorted(record, key = lambda x: (x[0], -x[1])):
            if current == 0:
                ans.append([time])
        
            current += target
            if current == 0:
                ans[-1].append(time)
                
        return ans
