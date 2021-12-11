class MyCalendar:

    def __init__(self):
        self.times = []
        

    def book(self, start: int, end: int) -> bool:
        
        startIndex, endIndex = bisect.bisect_right(self.times, start), bisect.bisect_left(self.times, end)
        if startIndex != endIndex or startIndex % 2 == 1:
            return False
        
        self.times.insert(startIndex, start)
        self.times.insert(endIndex + 1, end)

        return True
        
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)