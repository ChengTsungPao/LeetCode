class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        record = []
        for start, end, color in segments:
            record.append((start, color))
            record.append((end, -color))
        
        ans = []
        record.sort()
        preTime = record[0][0]
        sumColor = 0
        
        for time, color in record:
            if preTime != time and sumColor > 0:
                ans.append([preTime, time, sumColor])
            sumColor += color
            preTime = time
                
        return ans