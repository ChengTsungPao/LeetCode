class MyCalendarThree:

    def __init__(self):
        self.times = []
        
    def book(self, start: int, end: int) -> int:
        self.times.append((start, 1))
        self.times.append((end, -1))
        
        ans = _sum = 0
        for time, target in sorted(self.times):
            _sum += target
            ans = max(ans, _sum)
            
        return ans
        

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)