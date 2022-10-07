from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.times = SortedDict()
        
    def book(self, start: int, end: int) -> int:
        self.times[start] = self.times.get(start, 0) + 1
        self.times[end] = self.times.get(end, 0) - 1
        
        ans = _sum = 0
        for target in self.times.values():
            _sum += target
            ans = max(ans, _sum)
            
        return ans
        

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)