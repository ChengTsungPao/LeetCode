class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        index = 0
        while index<len(intervals)-1:
            if(intervals[index][1] >= intervals[index+1][0]):
                if(intervals[index][1] <= intervals[index+1][1]):
                    intervals[index][1] = intervals[index+1][1]                    
                del intervals[index+1]
            else:
                index += 1
        return intervals