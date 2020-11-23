class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        Interval = []
        for i in range(len(intervals)):
            for _ in range(len(newInterval)):
                if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                    Interval.append(intervals[i][-len(newInterval)])
                    del newInterval[0]
                    flag = True
                elif newInterval[0] <= intervals[i][0]:
                    Interval.append(newInterval[0])
                    del newInterval[0]
                    flag = False
            if len(Interval) == 2:
                ans += [Interval] + intervals[i + flag:]
                break
            if len(Interval) != 1:
                ans += [intervals[i]]
        return ans + [Interval + newInterval] * (len(Interval) != 2 or intervals == [])